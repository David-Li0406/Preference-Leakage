import matplotlib.pyplot as plt
import numpy as np

# Data from the figure
models = ["GPT-4o", "LLaMA-3.3", "Gemini-1.5"][::-1]

# Data from the figure
data = {
    "Mistral-7B":{
        "Mistral-GPT4o vs Mistral-Gemini-1.5": {
            "Gemini-1.5": [36.8, 63.2],
            "LLaMA-3.3": [49.5,50.5],
            "GPT4o": [55.1, 44.9],
        },
        "Mistral-GPT4o vs Mistral-LLaMA-3.3": {
            "Gemini-1.5": [65.8,34.2],
            "LLaMA-3.3": [60.3,39.7],
            "GPT4o": [61.6,38.4],
        },
        "Mistral-LLaMA-3.3 vs Mistral-Gemini-1.5": {
            "Gemini-1.5": [22.6,77.4],
            "LLaMA-3.3": [39.5,60.5],
            "GPT4o": [43.1,56.9],
        },
    },
    "Qwen-2.5-14B":{
        "Qwen-GPT4o vs Qwen-Gemini-1.5": {
            "Gemini-1.5": [39.3, 60.7],
            "LLaMA-3.3": [ 52.4, 47.6],
            "GPT4o": [57.8, 42.2],
        },
        "Qwen-GPT4o vs Qwen-LLaMA-3.3": {
            "Gemini-1.5": [63.3,36.7],
            "LLaMA-3.3": [59.3,40.7],
            "GPT4o": [61.5,38.5],
        },
        "Qwen-LLaMA-3.3 vs Qwen-Gemini-1.5": {
            "Gemini-1.5": [26.2,73.8],
            "LLaMA-3.3": [42.9,57.1],
            "GPT4o": [50.1,49.9],
        },
    }
}

def plot_pairwise_comparison(win_all, loss_all, title):
    # Plotting the bars in each subplot
    ax.barh(indices_spaced, win_all, height=bar_width, color="#497EAF", edgecolor="#497EAF", label="Model A Wins")
    # ax.barh(indices_spaced, tie_all, left=win_all, height=bar_width, color="#5B9BD4", edgecolor="#5B9BD4", label="Tie")
    ax.barh(indices_spaced, loss_all, left=win_all, height=bar_width, color="#ACC5E4", edgecolor="#ACC5E4", label="Model B Wins")


    # Adding labels to the bars
    for i, (wins, loses) in enumerate(zip(win_all, loss_all)):
        ax.text(wins / 2, indices_spaced[i], f"{wins:.1f}%", va="center", ha="center", color="white", fontsize=14)
        # ax.text(wins + ties / 2, indices_spaced[i], f"{ties:.1f}%", va="center", ha="center", color="white", fontsize=14)
        ax.text(wins + loses / 2, indices_spaced[i], f"{loses:.1f}%", va="center", ha="center", color="black", fontsize=14)

    # Adding labels and removing axes sides but keeping ticks
    ax.set_yticks(indices_spaced)
    ax.set_yticklabels(models, fontsize=16)
    ax.set_xticklabels(["0.0%", "20.0%", "40.0%", "60.0%", "80.0%", "100.0%"], fontsize=15)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.grid(False)
    ax.set_title(title,fontsize=16, fontweight='bold')


# Setting up bar positions
bar_width = 0.7 # Reduced bar width
indices = np.arange(len(models))
bar_spacing = 0.0 # Space between bars in indices
indices_spaced = indices * (1 + bar_spacing)


# Creating a figure with 2 rows and 3 columns of subplots
fig, axs = plt.subplots(2, 3, figsize=(21, 7), sharey=True, gridspec_kw={'hspace': 0.6})

#-------------------------------------
# Plotting for the Top 3 Models (Top-Left subplot)
#-------------------------------------
ax = axs[0, 0]  # Access the subplot at row 0, column 0
mistral_gpt4_gemini = data["Mistral-7B"]["Mistral-GPT4o vs Mistral-Gemini-1.5"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
loss_all = [v[1] for v in mistral_gpt4_gemini.values()]
title = "Mistral-GPT4o vs Mistral-Gemini-1.5"
plot_pairwise_comparison(win_all, loss_all, title)

#-------------------------------------
# Plotting for the Bottom 3 Models (Top-Middle Subplot)
#-------------------------------------
ax = axs[0, 1]  # Access the subplot at row 0, column 1
mistral_gpt4_gemini = data["Mistral-7B"]["Mistral-GPT4o vs Mistral-LLaMA-3.3"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
loss_all = [v[1] for v in mistral_gpt4_gemini.values()]
title = "Mistral-GPT4o vs Mistral-LLaMA-3.3"
plot_pairwise_comparison(win_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models again (Top-Right Subplot)
#-------------------------------------
ax = axs[0, 2]  # Access the subplot at row 0, column 2
mistral_gpt4_gemini = data["Mistral-7B"]["Mistral-LLaMA-3.3 vs Mistral-Gemini-1.5"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
loss_all = [v[1] for v in mistral_gpt4_gemini.values()]
title = "Mistral-LLaMA-3.3 vs Mistral-Gemini-1.5"
plot_pairwise_comparison(win_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models (Bottom-Left subplot)
#-------------------------------------
ax = axs[1, 0]  # Access the subplot at row 1, column 0
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["Qwen-GPT4o vs Qwen-Gemini-1.5"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
loss_all = [v[1] for v in qwen_gpt4_gemini.values()]
title = "Qwen-GPT4o vs Qwen-Gemini-1.5"
plot_pairwise_comparison(win_all, loss_all, title)
ax.text(-30, max(indices_spaced), "Judge Model", fontsize=18, fontweight="bold", ha="left", va="bottom", rotation=90)

#-------------------------------------
# Plotting for the Bottom 3 Models (Bottom-Middle Subplot)
#-------------------------------------
ax = axs[1, 1]  # Access the subplot at row 1, column 1
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["Qwen-GPT4o vs Qwen-LLaMA-3.3"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
loss_all = [v[1] for v in qwen_gpt4_gemini.values()]
title = "Qwen-GPT4o vs Qwen-LLaMA-3.3"
plot_pairwise_comparison(win_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models again (Bottom-Right Subplot)
#-------------------------------------
ax = axs[1, 2] # Access the subplot at row 1, column 2
# Plotting the bars in each subplot
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["Qwen-LLaMA-3.3 vs Qwen-Gemini-1.5"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
loss_all = [v[1] for v in qwen_gpt4_gemini.values()]
title = "Qwen-LLaMA-3.3 vs Qwen-Gemini-1.5"
plot_pairwise_comparison(win_all, loss_all, title)

# Adding a shared title above the subplots
# fig.suptitle("Comparison of Auto-J Performance Across Models", fontsize=18)

# Adding titles to the top and bottom rows
fig.text(0.52, 0.545, "(a). Mistral-7B", ha="center", fontsize=18)
fig.text(0.52, 0.08, "(b). Qwen-2.5-14B", ha="center", fontsize=18)

# Adding a shared legend
handles, labels = axs[0,0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.52, -0.024), ncol=3, frameon=False, fontsize=16)

# Adjust layout
plt.subplots_adjust(left=0.085, right=0.99, top=0.92, bottom=0.17, wspace=0.1, hspace=0.5)
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Display the plot
# plt.show()
plt.savefig("alpacaeval_result.pdf", format="pdf", dpi=800)