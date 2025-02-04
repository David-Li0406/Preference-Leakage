import matplotlib.pyplot as plt
import numpy as np

# Data from the figure
models = ["GPT-4", "Human"][::-1]

# Data from the figure
data = {
    "LLaMA-2 vs Others": {
        "Human": [73.6, 8.8, 17.6],
        "GPT4": [79.5, 1.7, 18.8],
    },
    "LLaMA-2 vs Claude-v1": {
        "Human": [76.2, 17.9, 6.0],
        "GPT4": [79.8, 20.2, 0.0],
    }
}

def plot_pairwise_comparison(win_all, tie_all, loss_all, title):
    # Plotting the bars in each subplot
    ax.barh(indices_spaced, win_all, height=bar_width, color="#497EAF", edgecolor="#497EAF", label="Model A Wins")
    ax.barh(indices_spaced, tie_all, left=win_all, height=bar_width, color="#5B9BD4", edgecolor="#5B9BD4", label="Tie")
    ax.barh(indices_spaced, loss_all, left=np.array(win_all) + np.array(tie_all), height=bar_width, color="#ACC5E4", edgecolor="#ACC5E4", label="Model B Wins")


    # Adding labels to the bars
    for i, (wins, ties, loses) in enumerate(zip(win_all, tie_all, loss_all)):
        ax.text(wins / 2, indices_spaced[i], f"{wins:.1f}%", va="center", ha="center", color="white", fontsize=22)
        ax.text(wins + ties / 2, indices_spaced[i], f"{ties:.1f}%", va="center", ha="center", color="white", fontsize=22)
        ax.text(wins + ties + loses / 2, indices_spaced[i], f"{loses:.1f}%", va="center", ha="center", color="black", fontsize=22)

    # Adding labels and removing axes sides but keeping ticks
    ax.set_yticks(indices_spaced)
    ax.set_yticklabels(models, fontsize=24)
    ax.set_xticklabels(["0.0%", "20.0%", "40.0%", "60.0%", "80.0%", "100.0%"], fontsize=24)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.grid(False)
    ax.set_title(title,fontsize=22, fontweight='bold')


# Setting up bar positions
bar_width = 0.7 # Reduced bar width
indices = np.arange(len(models))
bar_spacing = 0.0 # Space between bars in indices
indices_spaced = indices * (1 + bar_spacing)


# Creating a figure with 2 rows and 3 columns of subplots
fig, axs = plt.subplots(2, 1, figsize=(11, 8), sharey=True, gridspec_kw={'hspace': 0.5})

#-------------------------------------
# Plotting for the Top 3 Models (Top-Left subplot)
#-------------------------------------
ax = axs[0]  # Access the subplot at row 0, column 0
mistral_gpt4_gemini = data["LLaMA-2 vs Others"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
tie_all = [v[1] for v in mistral_gpt4_gemini.values()]
loss_all = [v[2] for v in mistral_gpt4_gemini.values()]
title = "LLaMA-2 vs Others"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

#-------------------------------------
# Plotting for the Bottom 3 Models (Top-Middle Subplot)
#-------------------------------------
ax = axs[1]  # Access the subplot at row 0, column 1
mistral_gpt4_gemini = data["LLaMA-2 vs Claude-v1"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
tie_all = [v[1] for v in mistral_gpt4_gemini.values()]
loss_all = [v[2] for v in mistral_gpt4_gemini.values()]
title = "LLaMA-2 vs Claude-v1"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)
ax.text(-20, max(indices_spaced), "Judge Model", fontsize=22, fontweight="bold", ha="left", va="bottom", rotation=90)

# Adding titles to the top and bottom rows
# fig.text(0.52, 0.545, "(a). Mistral-7B", ha="center", fontsize=24)
# fig.text(0.52, 0.08, "(b). Qwen-2.5-14B", ha="center", fontsize=24)

# Adding a shared legend
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.52, -0.024), ncol=3, frameon=False, fontsize=22)

# Adjust layout
plt.subplots_adjust(left=0.16, right=0.98, top=0.92, bottom=0.17, wspace=0.1, hspace=0.5)
# plt.tight_layout(rect=[0, 0.05, 1, 0.95])

# Display the plot
# plt.show()
plt.savefig("llama_mtbench_result.pdf", format="pdf", dpi=800)