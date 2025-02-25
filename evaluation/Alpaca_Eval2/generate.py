import torch
import datasets
from transformers import AutoTokenizer, AutoModelForCausalLM

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained("/local/sunrenliang/pre_trained_models/llama-1b")
model = AutoModelForCausalLM.from_pretrained("/local/sunrenliang/pre_trained_models/llama-1b")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

if tokenizer.pad_token_id is None:
    tokenizer.pad_token_id = tokenizer.eos_token_id

def generate(instruction):
    input_ids = tokenizer.encode(instruction, return_tensors="pt")
    input_ids = input_ids.to(device)
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long, device=device)
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=4096, num_return_sequences=1)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

eval_set = datasets.load_dataset("tatsu-lab/alpaca_eval", "alpaca_eval")["eval"]

# 限制生成的样本数量
num_examples_to_generate = 1

for i, example in enumerate(eval_set):
    if i >= num_examples_to_generate:
        break
    example["output"] = generate(example["instruction"])
    example["generator"] = "LLaMA"

    # 打印结果示例
    print(f"Instruction: {example['instruction']}")
    print(f"Output: {example['output']}")
    print(f"Generator: {example['generator']}")
    print(f"Dataset: {example['dataset']}")
    print(f"Datasplit: {example['datasplit']}")
    print("-" * 50)

#for example in eval_set:
    # generate here is a placeholder for your models generations
    #example["output"] = generate(example["instruction"])
    #example["generator"] = "llama-1b" # name of your model
    #break

#for example in eval_set:
    #print(f"Instruction: {example['instruction']}")
    #print(f"Output: {example['output']}")
    #print(f"Generator: {example['generator']}")
    #print("-" * 50)
    #break
