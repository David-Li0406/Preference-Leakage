import matplotlib.pyplot as plt
import numpy as np

# Data from the figure
models = ["GPT-4o", "LLaMA-3.3", "Gemini-1.5"][::-1]

# Data from the figure
data = {
    "Mistral-7B":{
        "GPT4o vs Gemini-1.5": {
            "Gemini-1.5": [18.2, 39.8, 42.0],
            "LLaMA-3.3": [27.4, 43.8, 28.8],
            "GPT4o": [38.4, 34.6, 27.0],
        },
        "GPT4o vs LLaMA-3.3": {
            "Gemini-1.5": [46.2, 42.7, 11.1],
            "LLaMA-3.3": [50.4, 35.0, 14.6],
            "GPT4o": [55.8, 27.0, 17.2],
        },
        "LLaMA-3.3 vs Gemini-1.5": {
            "Gemini-1.5": [9.2, 31.4, 59.4],
            "LLaMA-3.3": [14.6, 30.0, 55.4],
            "GPT4o": [22.2, 30.8, 47.0],
        },
    },
    "Qwen-2.5-14B":{
        "GPT4o vs Gemini-1.5": {
            "Gemini-1.5": [22.0, 33.5, 44.5],
            "LLaMA-3.3": [28.8, 50.2, 21.6],
            "GPT4o": [49.8, 29.0, 21.2],
        },
        "GPT4o vs LLaMA-3.3": {
            "Gemini-1.5": [52.1, 40.7, 7.2],
            "LLaMA-3.3": [39.0, 51.8, 9.2],
            "GPT4o": [57.4, 29.6, 13.0],
        },
        "LLaMA-3.3 vs Gemini-1.5": {
            "Gemini-1.5": [10.0, 29.4, 60.6],
            "LLaMA-3.3": [16.4, 48.4, 35.2],
            "GPT4o": [24.6, 30.0, 44.4],
        },
    }
}

def plot_pairwise_comparison(win_all, tie_all, loss_all, title):
    # Plotting the bars in each subplot
    ax.barh(indices_spaced, win_all, height=bar_width, color="#497EAF", edgecolor="#497EAF", label="Model A Wins")
    ax.barh(indices_spaced, tie_all, left=win_all, height=bar_width, color="#5B9BD4", edgecolor="#5B9BD4", label="Tie")
    ax.barh(indices_spaced, loss_all, left=np.array(win_all) + np.array(tie_all), height=bar_width, color="#ACC5E4", edgecolor="#ACC5E4", label="Model B Wins")


    # Adding labels to the bars
    for i, (wins, ties, loses) in enumerate(zip(win_all, tie_all, loss_all)):
        ax.text(wins / 2, indices_spaced[i], f"{wins:.1f}%", va="center", ha="center", color="white", fontsize=14)
        ax.text(wins + ties / 2, indices_spaced[i], f"{ties:.1f}%", va="center", ha="center", color="white", fontsize=14)
        ax.text(wins + ties + loses / 2, indices_spaced[i], f"{loses:.1f}%", va="center", ha="center", color="black", fontsize=14)

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
mistral_gpt4_gemini = data["Mistral-7B"]["GPT4o vs Gemini-1.5"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
tie_all = [v[1] for v in mistral_gpt4_gemini.values()]
loss_all = [v[2] for v in mistral_gpt4_gemini.values()]
title = "Mistral-GPT4o vs Mistral-Gemini-1.5"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

#-------------------------------------
# Plotting for the Bottom 3 Models (Top-Middle Subplot)
#-------------------------------------
ax = axs[0, 1]  # Access the subplot at row 0, column 1
mistral_gpt4_gemini = data["Mistral-7B"]["GPT4o vs LLaMA-3.3"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
tie_all = [v[1] for v in mistral_gpt4_gemini.values()]
loss_all = [v[2] for v in mistral_gpt4_gemini.values()]
title = "Mistral-GPT4o vs Mistral-LLaMA-3.3"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models again (Top-Right Subplot)
#-------------------------------------
ax = axs[0, 2]  # Access the subplot at row 0, column 2
mistral_gpt4_gemini = data["Mistral-7B"]["LLaMA-3.3 vs Gemini-1.5"]
win_all = [v[0] for v in mistral_gpt4_gemini.values()]
tie_all = [v[1] for v in mistral_gpt4_gemini.values()]
loss_all = [v[2] for v in mistral_gpt4_gemini.values()]
title = "Mistral-LLaMA-3.3 vs Mistral-Gemini-1.5"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models (Bottom-Left subplot)
#-------------------------------------
ax = axs[1, 0]  # Access the subplot at row 1, column 0
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["GPT4o vs Gemini-1.5"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
tie_all = [v[1] for v in qwen_gpt4_gemini.values()]
loss_all = [v[2] for v in qwen_gpt4_gemini.values()]
title = "Qwen-GPT4o vs Qwen-Gemini-1.5"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)
ax.text(-30, max(indices_spaced), "Judge Model", fontsize=18, fontweight="bold", ha="left", va="bottom", rotation=90)

#-------------------------------------
# Plotting for the Bottom 3 Models (Bottom-Middle Subplot)
#-------------------------------------
ax = axs[1, 1]  # Access the subplot at row 1, column 1
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["GPT4o vs LLaMA-3.3"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
tie_all = [v[1] for v in qwen_gpt4_gemini.values()]
loss_all = [v[2] for v in qwen_gpt4_gemini.values()]
title = "Qwen-GPT4o vs Qwen-LLaMA-3.3"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

#-------------------------------------
# Plotting for the Top 3 Models again (Bottom-Right Subplot)
#-------------------------------------
ax = axs[1, 2] # Access the subplot at row 1, column 2
# Plotting the bars in each subplot
qwen_gpt4_gemini = data["Qwen-2.5-14B"]["LLaMA-3.3 vs Gemini-1.5"]
win_all = [v[0] for v in qwen_gpt4_gemini.values()]
tie_all = [v[1] for v in qwen_gpt4_gemini.values()]
loss_all = [v[2] for v in qwen_gpt4_gemini.values()]
title = "Qwen-LLaMA-3.3 vs Qwen-Gemini-1.5"
plot_pairwise_comparison(win_all, tie_all, loss_all, title)

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
plt.savefig("arenahard_result.pdf", format="pdf", dpi=800)