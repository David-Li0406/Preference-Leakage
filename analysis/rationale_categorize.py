import os
import json
import argparse
from tqdm import tqdm
from utils import *
import re


template='''Given a pairwise comparison judgment made by an AI, please categorize each considered aspect in the rationale to one of the following categories:

{{
    "Factuality": "Whether the information provided in the response is accurate, based on reliable facts and data.",
    "User Satisfaction": "Whether the response meets the user's question and needs, and provides a comprehensive and appropriate answer to the question.",
    "Logical Coherence": "Whether the response maintains overall consistency and logical coherence between different sections, avoiding self-contradiction.",
    "Richness": "Whether the response includes rich info, depth, context, diversity, detailed explanations and examples to meet user needs and provide a comprehensive understanding.",
    "Creativity": "Whether the response is innovative or unique, providing novel insights or solutions.",
    "Fairness and Responsibility": "Whether the advice or information provided in the response is feasible, carries acertain degree of responsibility, and considers potential risks and consequences.",
    "Completeness": "Whether the response provides sufficient information and details to meet the user's needs, and whether it avoids omitting important aspects.",
    "Clarity": "Whether the response is clear and understandable, and whether it uses concise language and structure so that the user can easily understand it.",
    "Others": "Other aspects which is not listed above."
}}

## Judgment: {}

Please output the generated content in a json format, for example:
{{
"Factuality": // list, all aspects that belong to this category, such as ["correctness", "mistakes"]
...
}}

Formatted the abovementioned schema and categorize aspects in the judgment:'''


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


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--judge_name', type=str, default='gemini')
    argparser.add_argument('--model1_name', type=str, default='gpt-4o')
    argparser.add_argument('--model2_name', type=str, default='gemini')
    args = argparser.parse_args()

    file_path = "arenaHard_result/{}-judge-{}-and-{}.jsonl".format(args.judge_name, args.model1_name, args.model2_name)
    if not os.path.exists(file_path):
        file_path = "arenaHard_result/{}-judge-{}-and-{}.jsonl".format(args.judge_name, args.model2_name, args.model1_name)

    judgment_result = []
    with open(file_path) as f:
        for line in f.readlines():
            judgment_result.append(json.loads(line))

    dataset_rationale = []
    for idx, item in tqdm(enumerate(judgment_result)):
        for game in item["games"]:
            judgment = game["judgment"]
            score = game["score"]
            prompt = template.format(judgment)
            response = generate_openai(messages=prompt, model="gpt-4o-2024-11-20")
            response_dict = extract(response)
            if isinstance(response_dict, dict):
                # print(response_dict)
                dataset_rationale.append({
                    "idx": idx,
                    "judgment": judgment,
                    "score": score,
                    "considered aspects": response_dict
                })

    with open("rationale_categorization/{}-judge-{}-and-{}-ArenaHard.json".format(args.judge_name, args.model1_name, args.model2_name), "w") as f:
        json.dump(dataset_rationale, f, indent=2) 


if __name__ == "__main__":
    main()