def spearman_correlation_calculation(rank_x, rank_y):
    if len(rank_x) != len(rank_y):
        raise ValueError("Input lists must have the same length.")
    
    n = len(rank_x)
    if n == 0:
        raise ValueError("Input lists must not be empty.")

    # Convert values to ranks if not already ranks
    def rankify(values):
        sorted_vals = sorted((val, idx) for idx, val in enumerate(values))
        ranks = [0] * len(values)
        i = 0
        while i < len(sorted_vals):
            j = i
            while j + 1 < len(sorted_vals) and sorted_vals[j+1][0] == sorted_vals[i][0]:
                j += 1
            avg_rank = (i + j + 2) / 2  # ranks are 1-based
            for k in range(i, j + 1):
                ranks[sorted_vals[k][1]] = avg_rank
            i = j + 1
        return ranks

    rank_x = rankify(rank_x)
    rank_y = rankify(rank_y)

    # Compute d_i and d_i^2
    d_squared_sum = sum((rx - ry) ** 2 for rx, ry in zip(rank_x, rank_y))
    
    # Spearman correlation formula
    return 1 - (6 * d_squared_sum) / (n * (n**2 - 1))

def extract_chatbot_arena():
    model_list = []
    with open("analysis/chatbot_arena_raw.txt") as f:
        for i, line in enumerate(f.readlines()):
            if (i-11) % 9 == 0:
                if line.strip() not in model_list:
                    model_list.append(line.strip())

    return model_list[1:]

def extract_alpacaeval():
    model_list = []
    with open("analysis/alpacaeval_raw.txt") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                continue
            model_list.append(line.split("\t")[1][:-2])
    
    return model_list

def difference(model_list_arena, model_list_alpacaeval):
    arena2alpacaeval = {
        "GPT-4o-2024-05-13": "GPT-4 Omni (05/13)",
        "GPT-4o-mini-2024-07-18": "GPT-4o Mini (07/18)",
        "Meta-Llama-3.1-405B-Instruct-bf16": "Llama 3.1 405B Instruct",
        "GPT-4-Turbo-2024-04-09": "GPT-4 Turbo (04/09)",
        "GPT-4-1106-preview": "GPT-4 Preview (11/06)",
        "Meta-Llama-3.1-70B-Instruct": "Llama 3.1 70B Instruct",
        "Claude 3 Opus": "Claude 3 Opus (02/29)",
        "Llama-3-70B-Instruct": "Llama 3 70B Instruct",
        "Claude 3 Sonnet": "Claude 3 Sonnet (02/29)",
        "Qwen2-72B-Instruct": "Qwen2 72B Instruct",
        "GPT-4-0314": "GPT-4 (03/14)",
        "Meta-Llama-3.1-8B-Instruct": "Llama 3.1 8B Instruct",
        "GPT-4-0613": "GPT-4 (06/13)",
        "Mistral-Large-2402": "Mistral Large (24/02)",
        "Llama-3-8B-Instruct": "Llama 3 8B Instruct",
        "Command R (04-2024)": "Cohere Command",
        "Mistral Medium": "Mistral Medium",
        "Mixtral-8x22b-Instruct-v0.1": "Mixtral 8x22B v0.1",
        "Qwen1.5-72B-Chat": "Qwen1.5 72B Chat",
        "Gemini Pro": "Gemini Pro",
        "Yi-34B-Chat": "Yi 34B Chat",
        "Mixtral-8x7B-Instruct-v0.1": "Mixtral 8x7B v0.1",
        "Qwen1.5-14B-Chat": "Qwen1.5 14B Chat",
        "GPT-3.5-Turbo-0125": "GPT 3.5 Turbo (03/01)",
        "DBRX-Instruct-Preview": "DBRX Instruct",
        "Tulu-2-DPO-70B": "Tulu 2+DPO 70B",
        "Llama-2-70B-chat": "LLaMA2 Chat 70B",
        "Vicuna-33B": "Vicuna 33B v1.3",
        "Gemma-1.1-7B-it": "Gemma Instruct (7B)",
        "OpenHermes-2.5-Mistral-7B": "OpenHermes-2.5-Mistral (7B)",
        "Mistral-7B-Instruct-v0.2": "Mistral 7B v0.2",
        "Qwen1.5-7B-Chat": "Qwen1.5 7B Chat",
        "GPT-3.5-Turbo-1106": "GPT 3.5 Turbo (11/06)",
        "Llama-2-13b-chat": "LLaMA2 Chat 13B",
        "WizardLM-13b-v1.2": "WizardLM 13B",
        "Vicuna-13B": "Vicuna 13B",
        "Llama-2-7B-chat": "LLaMA2 Chat 7B",
        "Guanaco-33B": "Guanaco 33B",
        "Vicuna-7B": "Vicuna 7B",
        "Gemma-2B-it": "Gemma Instruct (2B)",
        "OpenAssistant-Pythia-12B": "Pythia 12B OASST SFT"
    }

    model_list_arena = [item for item in model_list_arena if item in arena2alpacaeval.keys()]
    model_list_alpacaeval = [item for item in model_list_alpacaeval if item in arena2alpacaeval.values()]


    model_list_arena_alpacaeval = [arena2alpacaeval[item] for item in model_list_arena]
    pl_models = {
        "self-bias": ["GPT-4 Preview (11/06)"],
        "preference leakage": ["Vicuna 33B v1.3", "Vicuna 7B", "Vicuna 13B"],
    }



    for leakage_type, models in pl_models.items():
        avg_difference = []
        for model in models:
            # if the ranking of a model in chatbot arena is larger than that in alpacaeval, it means alpacaeval prefer that model, hinting there is a preference bias
            avg_difference.append(model_list_arena_alpacaeval.index(model) - model_list_alpacaeval.index(model))
        avg_difference = sum(avg_difference)/len(avg_difference)
        print("{}: {}".format(leakage_type, avg_difference))


if __name__ == "__main__":
    model_list_arena = extract_chatbot_arena()
    model_list_alpacaeval = extract_alpacaeval()
    difference(model_list_arena, model_list_alpacaeval)