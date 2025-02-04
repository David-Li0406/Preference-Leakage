from datasets import load_dataset, Dataset
from transformers import AutoTokenizer
from transformers import DataCollatorWithPadding
import evaluate
import numpy as np
from sklearn.model_selection import train_test_split
import json

id2label = {0: "gpt4", 1: "gemini", 2: "llama"}
label2id = {"gpt4": 0, "gemini": 1, "llama": 2}

def build_dataset():
    template="alpacaEval/output_Mistral-7B-v0.1_{}_sft.json"
    judge_models = ["gpt4", "gemini", "llama"]
    judge2data = {judge_model: json.load(open(template.format(judge_model))) for judge_model in judge_models}
    testset = []
    for i in range(len(judge2data["gpt4"])):
        for judge_model in judge_models:
            item = {
                "text": judge2data[judge_model][i]["output"],
                "label": label2id[judge_model]
            }
            testset.append(item)

    return testset

all_dataset = build_dataset()
dataset_train, dataset_test, _, _ = train_test_split(
    all_dataset, [0 for _ in all_dataset], test_size=0.2, random_state=42
)

dataset_train = {
    "text": [item["text"] for item in dataset_train],
    "label": [item["label"] for item in dataset_train]
}

dataset_test = {
    "text": [item["text"] for item in dataset_test],
    "label": [item["label"] for item in dataset_test]
}

dataset_train, dataset_test = Dataset.from_dict(dataset_train), Dataset.from_dict(dataset_test)

# imdb = load_dataset("imdb")
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")

def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized_dataset_train = dataset_train.map(preprocess_function, batched=True)

tokenized_dataset_test = dataset_test.map(preprocess_function, batched=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

accuracy = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)


from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer


model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-uncased", num_labels=3, id2label=id2label, label2id=label2id
)


training_args = TrainingArguments(
    output_dir="saves/bert_classifier",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    push_to_hub=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset_train,
    eval_dataset=tokenized_dataset_test,
    processing_class=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()