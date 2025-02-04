import torch
import datasets
from transformers import AutoTokenizer, AutoModelForCausalLM
import argparse
import json
from tqdm import tqdm

def generate(instruction, tokenizer, model, device):
    input_ids = tokenizer.encode(instruction, return_tensors="pt")
    input_ids = input_ids.to(device)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=device)
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=4096, num_return_sequences=1)
    input_len = input_ids.shape[-1]
    generated_text = tokenizer.decode(output[0][input_len:], skip_special_tokens=True)
    return generated_text.strip()


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--model_name', type=str, default='Mistral-7B-v0.1')
    argparser.add_argument('--judge_name', type=str, default='llama')
    argparser.add_argument('--tuning_technique', type=str, default='sft')
    argparser.add_argument('--exp', type=str, default='')
    argparser.add_argument('--ratio', type=float, default=0.0)
    args = argparser.parse_args()

    if args.exp == "":
        model_path = "saves/{}/{}_{}_30000".format(args.model_name, args.judge_name, args.tuning_technique)
    else:
        if args.ratio == 0.0:
            model_path = "saves/{}/{}_{}_30000_{}".format(args.model_name, args.judge_name, args.tuning_technique, args.exp)
        else:
            model_path = "saves/{}/{}/{}_{}_{}".format(args.model_name, args.exp, args.judge_name, args.tuning_technique, str(args.ratio))
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
        ret = generate(instruction1, tokenizer, model, device)
        if ret == "":
            ret = generate(instruction2, tokenizer, model, device)
        example["output"] = ret
        example["generator"] = "{}_{}_{}".format(args.model_name, args.judge_name, args.tuning_technique)
        output_all.append(example)

    if args.exp == "":
        with open("alpacaEval/output_{}_{}_{}.json".format(args.model_name, args.judge_name, args.tuning_technique), "w") as f:
            json.dump(output_all, f, indent=2)
    else:
        if args.ratio == 0.0:
            with open("alpacaEval/output_{}_{}_{}_{}.json".format(args.model_name, args.judge_name, args.tuning_technique, args.exp), "w") as f:
                json.dump(output_all, f, indent=2)
        else:
            with open("alpacaEval/output_{}_{}_{}_{}_{}.json".format(args.model_name, args.judge_name, args.tuning_technique, args.exp, str(args.ratio)), "w") as f:
                json.dump(output_all, f, indent=2)


if __name__ == "__main__":
    main()