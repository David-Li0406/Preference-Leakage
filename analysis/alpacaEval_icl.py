import torch
import datasets
from transformers import AutoTokenizer, AutoModelForCausalLM
import argparse
import json
from tqdm import tqdm
import random
random.seed(42)
import os

template='''Follow the given demonstration to answer the question.

{}

Below is the question to be answered:

## Instruction: {}

Output: '''

def generate(instruction, tokenizer, model, device):
    input_ids = tokenizer.encode(instruction, return_tensors="pt")
    input_ids = input_ids.to(device)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=device)
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=4096, num_return_sequences=1)
    input_len = input_ids.shape[-1]
    generated_text = tokenizer.decode(output[0][input_len:], skip_special_tokens=True)
    return generated_text.strip()


def load_demonstration(args):
    synthetic_data = json.load(open("data/UltraFeedback_sampled_30000_{}_LlamaFactory.json".format(args.judge_name)))
    demonstration_list = random.sample(synthetic_data, 4)
    demonstration_str = ''
    for i, demonstration in enumerate(demonstration_list):
        demonstration_str += '''

## Example {}:

## Instruction: {}

## Output: {}'''.format(str(i+1), demonstration["instruction"], demonstration["output"])

    return demonstration_str

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--model_name', type=str, default='Mistral-7B-v0.1')
    argparser.add_argument('--judge_name', type=str, default='gemini')
    argparser.add_argument('--tuning_technique', type=str, default='sft')
    argparser.add_argument('--exp', type=str, default='')
    argparser.add_argument('--ratio', type=float, default=0.0)
    args = argparser.parse_args()

    demonstration_str = load_demonstration(args)
    with open("demonstration/{}.json".format(args.judge_name), "w") as f:
        json.dump({"demonstration":demonstration_str},f,indent=2)
    exit()

    model_path = "/scratch/daweili5/preference_leakage/saves/Mistral-7B-v0.1/moss_oasst_lima_sft_30000"
    model = AutoModelForCausalLM.from_pretrained(model_path)


    tokenizer = AutoTokenizer.from_pretrained(model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    eval_set = datasets.load_dataset("tatsu-lab/alpaca_eval", "alpaca_eval", trust_remote_code=True)["eval"]

    output_all = []
    for i, example in tqdm(enumerate(eval_set)):
        instruction1 = "[INST] {} [/INST]".format(example["instruction"])
        instruction2 = "{} Output: ".format(example["instruction"])
        instruction1 = template.format(demonstration_str, instruction1)
        ret = generate(instruction1, tokenizer, model, device)
        if ret == "":
            instruction2 = template.format(demonstration_str, instruction2)
            ret = generate(instruction2, tokenizer, model, device)
        example["output"] = ret
        example["generator"] = "Mistral-7B-v0.1_{}_moss_oasst_lima_sft_icl.json".format(args.judge_name)
        output_all.append(example)

    with open("alpacaEval/output_Mistral-7B-v0.1_{}_moss_oasst_lima_sft_icl.json".format(args.judge_name), "w") as f:
            json.dump(output_all, f, indent=2)

if __name__ == "__main__":
    main()