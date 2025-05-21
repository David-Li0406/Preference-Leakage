import matplotlib.pyplot as plt
import numpy as np

# Data from the image
students = [
    "Qwen-2.5-3B", "Qwen-2.5-7B", "Qwen-2.5-14B",
    "Qwen-3-1.7B", "Qwen-3-4B", "Qwen-3-8B", "Qwen-3-14B"
]
alpaca_eval = [20.1, 22.1, 18.6, 20.1, 17.2, 17.4, 19.4]
arena_hard = [50.7, 32.2, 37.1, 40.0, 30.9, 33.9, 31.7]
# avg_scores = [35.4, 27.2, 27.9, 30.2, 24.1, 25.7, 25.6]

x = np.arange(len(students))  # the label locations
width = 0.4  # the width of the bars

# Create the bar chart without the 'Avg' results and with updated colors
fig, ax = plt.subplots(figsize=(8, 6))
rects1 = ax.bar(x - width / 2, alpaca_eval, width, label='AlpacaEval 2.0', color='#1F77B6')
rects2 = ax.bar(x + width / 2, arena_hard, width, label='ArenaHard', color='#FF7E09')

# Add labels, title and legend
ax.set_ylabel('PL Score',fontsize=16)
# ax.set_title('Evaluation Scores by Model and Metric (Without Avg)',fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(students, rotation=45,fontsize=16)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=16)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.5, linewidth=2)

for spine in ax.spines.values():
    spine.set_linewidth(2)

ax.tick_params(axis='both', width=2)

plt.tight_layout()
# plt.show()
plt.savefig("size.pdf", format="pdf", dpi=800)
