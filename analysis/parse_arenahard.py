import json
import os
import argparse


def parse_result(judge_models, template):
    for judge_model in judge_models:
        for model_pair in [["gpt-4o", "gemini"], ["gpt-4o", "llama"], ["llama", "gemini"], ["gemini", "gpt-4o"], ["llama", "gpt-4o"], ["gemini", "llama"]]:
            modelA = model_pair[0]
            modelB = model_pair[1]
            modelA_win, modelB_win, tie = 0, 0, 0
            count = 0
            if not os.path.exists(template.format(judge_model, modelA, modelB)):
                continue
            with open(template.format(judge_model, modelA, modelB), encoding="utf8") as f:
                for line in f.readlines():
                    count += 1
                    item = json.loads(line)
                    if (modelA == "gpt-4o" and modelB == "gemini") or (modelA == "gemini" and modelB == "gpt-4o"):
                        if item['games'][0]['score'] in ["A>B", "A>>B"] and item['games'][1]['score'] in ["B>A", "B>>A"]:
                            modelB_win += 1
                        elif item['games'][0]['score'] in ["B>A", "B>>A"] and item['games'][1]['score'] in ["A>B", "A>>B"]:
                            modelA_win += 1
                        else:
                            tie += 1
                        
                    elif modelA == "gpt-4o" and modelB == "llama":
                        if item['games'][0]['score'] in ["A>B", "A>>B"] and item['games'][1]['score'] in ["B>A", "B>>A"]:
                            modelA_win += 1
                        elif item['games'][0]['score'] in ["B>A", "B>>A"] and item['games'][1]['score'] in ["A>B", "A>>B"]:
                            modelB_win += 1
                        else:
                            tie += 1
                            
                    elif modelA == "llama" and modelB == "gemini":
                        if item['games'][0]['score'] in ["A>B", "A>>B"] and item['games'][1]['score'] in ["B>A", "B>>A"]:
                            modelB_win += 1
                        elif item['games'][0]['score'] in ["B>A", "B>>A"] and item['games'][1]['score'] in ["A>B", "A>>B"]:
                            modelA_win += 1
                        else:
                            tie += 1
            
                    

            print("{} vs {}".format(modelA, modelB))
            print("judge model: ", judge_model)
            print("{} win: {}".format(modelA, modelA_win/count))
            print("{} win: {}".format(modelB, modelB_win/count))
            print("tie: ", tie/count)
            print("=============================")


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--sft', action='store_true')
    argparser.add_argument('--inherit', action='store_true')
    argparser.add_argument('--dpo', action='store_true')
    argparser.add_argument('--same_family', action='store_true')
    argparser.add_argument('--icl', action='store_true')
    argparser.add_argument('--mix', action='store_true')
    args = argparser.parse_args()

    if args.sft:
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}.jsonl"
        judge_models = ["gemini", "GPT-4o", "Llama3-70B"]
        parse_result(judge_models, template)
    elif args.same_family:
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}.jsonl"
        judge_models = ["gemini-1.5-pro", "GPT-4-turbo"]
        parse_result(judge_models, template)
        judge_models = ["gemini-1.0-pro", "chatgpt"]
        parse_result(judge_models, template)
    elif args.dpo:
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-dpo.jsonl"
        judge_models = ["gemini", "GPT-4o"]
        parse_result(judge_models, template)
    elif args.inherit:
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-inherit.jsonl"
        judge_models = ["gemini", "GPT-4o"]
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-inherit-new.jsonl"
        parse_result(judge_models, template)
    elif args.icl:
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-icl.jsonl"
        judge_models = ["gemini", "GPT-4o"]
        parse_result(judge_models, template)
    elif args.mix:
        judge_models = ["gemini", "GPT-4o"]
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-0.1.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-0.3.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-0.5.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-0.7.jsonl"
        parse_result(judge_models, template)

        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-synthetic-0.1.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-synthetic-0.3.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-synthetic-0.5.jsonl"
        parse_result(judge_models, template)
        template = "analysis/arenaHard_result/{}-judge-{}-and-{}-mix-synthetic-0.7.jsonl"
        parse_result(judge_models, template)

if __name__ == "__main__":
    main()