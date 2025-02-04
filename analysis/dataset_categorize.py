import os
import json
import argparse
from tqdm import tqdm
from utils import *
import re


template='''Given a question, please categorize it to one of the following categories:

1. Computer Science & Programming
2. Mathematics & Statistics
3. Science & Engineering
4. Business & Finance
5. Writing & Communication
6. Social & Daily Life
7. Others

## Question: {}

Please output the generated content in a json format, for example:
{{
"question category": // string, specific category name, such as "Computer Science & Programming"
}}

Formatted the abovementioned schema and categorize the given question:'''


def extract(context):
    # Preprocess context: escape triple-quoted strings
    preprocessed_context = re.sub(r"'''(.*?)'''", lambda m: json.dumps(m.group(1)), context, flags=re.DOTALL).replace("\n", "")

    # Match content between the outermost curly braces that may represent a JSON object
    pattern = r'\{[^{}]*\}'
    matches = re.findall(pattern, preprocessed_context)

    for match in matches:
        try:
            # Try to parse each match as JSON
            extracted_dict = json.loads(match)
            return extracted_dict  # Return the first valid JSON found
        except json.JSONDecodeError as e:
            # If parsing fails, continue to check the next match
            continue
    
    return None


def alpacaeval():
    data = json.load(open("dataset_categorization/alpacaeval.json"))

    dataset_categorization = []
    for idx, item in tqdm(enumerate(data)):
        question = item["instruction"]
        prompt = template.format(question)
        response = generate_openai(messages=prompt, model="gpt-4o-2024-11-20")
        response_dict = extract(response)
        if isinstance(response_dict, dict):
            dataset_categorization.append({
                "idx": idx,
                "question": question,
                "categorization": response_dict
            })

    with open("dataset_categorization/alpacaeval_categorization.json", "w") as f:
        json.dump(dataset_categorization, f, indent=2) 


def arenahard():
    data = []
    with open("dataset_categorization/question.jsonl") as f:
        for line in f.readlines():
            data.append(json.loads(line))
        
    
    dataset_categorization = []
    for idx, item in tqdm(enumerate(data)):
        assert len(item["turns"]) == 1
        question = item["turns"][0]["content"]
        prompt = template.format(question)
        response = generate_openai(messages=prompt, model="gpt-4o-2024-11-20")
        response_dict = extract(response)
        if isinstance(response_dict, dict):
            dataset_categorization.append({
                "idx": idx,
                "question": question,
                "categorization": response_dict
            })

    with open("dataset_categorization/arenahard_categorization.json", "w") as f:
        json.dump(dataset_categorization, f, indent=2)


if __name__ == "__main__":
    alpacaeval()
    arenahard()