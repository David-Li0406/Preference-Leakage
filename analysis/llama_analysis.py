from datasets import load_dataset
import json

def analyze_mtbench():
    # Load the dataset
    dataset = load_dataset("lmsys/mt_bench_human_judgments")

    # Access the train split (if applicable)
    train_human = dataset['human']
    train_gpt4 = dataset['gpt4_pair']

    win, loss, tie = 0, 0, 0
    win_human, loss_human, tie_human = 0, 0, 0

    key2human = {}
    for item in train_human:
        idx, model_a, model_b, turn = str(item["question_id"]), item["model_a"], item["model_b"], str(item["turn"])
        key2human[idx + model_a + model_b + turn] = item

    count = 0
    for item in train_gpt4:
        idx, model_a, model_b, turn = str(item["question_id"]), item["model_a"], item["model_b"], str(item["turn"])
        if (model_a == "llama-13b" and model_b == "claude-v1") or (model_b == "llama-13b" and model_a == "claude-v1"):
            if idx + model_a + model_b + turn in key2human:
                count += 1
                item_human = key2human[idx + model_a + model_b + turn]
                
                if "alpaca" in model_a:
                    if item["winner"] == "model_a":
                        win += 1
                    elif item["winner"] == "model_b":
                        loss += 1
                    else:
                        tie += 1
                else:
                    if item["winner"] == "model_a":
                        loss += 1
                    elif item["winner"] == "model_b":
                        win += 1
                    else:
                        tie += 1

                if "alpaca" in item_human["model_a"]:
                    if item_human["winner"] == "model_a":
                        win_human += 1
                    elif item_human["winner"] == "model_b":
                        loss_human += 1
                    else:
                        tie_human += 1
                else:
                    if item_human["winner"] == "model_a":
                        loss_human += 1
                    elif item_human["winner"] == "model_b":
                        win_human += 1
                    else:
                        tie_human += 1

                # print(item)
                # print(item_human)
                # print(win, win_human)
                # exit()

    print("gpt4-pair:")
    print("win:", win/(win+loss+tie))
    print("loss:", loss/(win+loss+tie))
    print("tie:", tie/(win+loss+tie))

    print("human:")
    print("win:", win_human/(win_human+loss_human+tie_human))
    print("loss:", loss_human/(win_human+loss_human+tie_human))
    print("tie:", tie_human/(win_human+loss_human+tie_human))

    print("total number:", count)

if __name__ == "__main__":
    analyze_mtbench()