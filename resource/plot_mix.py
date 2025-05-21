import matplotlib.pyplot as plt

# Data
x = [10, 30, 50, 70, 100]
alpacaeval_human = [3.6, 6.9, 8.3, 12.4, 18.4]
arenahard_human = [12.1, 13.6, 22.0, 24.8, 28.7]
alpacaeval_syn = [-0.8, 3.1, 8.1, 9.6, 18.4]
arenahard_syn = [0.5, 4.1, 13.7, 16.9, 28.7]

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, alpacaeval_human, marker='o', color="#2770B3", label='AlpacaEval2.0 - Manual', linewidth=3, markersize=8)
ax.plot(x, arenahard_human, marker='s', color="#EB661E", label='ArenaHard - Manual', linewidth=3, markersize=8)
ax.plot(x, alpacaeval_syn, marker='v', color="#2770B3", linestyle="--", label='AlpacaEval2.0 - Synthetic', linewidth=3, markersize=8)
ax.plot(x, arenahard_syn, marker='d', color="#EB661E", linestyle="--", label='ArenaHard - Synthetic', linewidth=3, markersize=8)

# Labels and title
ax.set_xlabel('Contamination Ratio (%)', fontsize=18)
ax.set_ylabel('Preference Leakage Score (%)', fontsize=18)

# Grid as dashed lines
ax.grid(True, linestyle='--', linewidth=2)

# Legend and ticks
ax.legend(fontsize=16)
ax.tick_params(axis='x', labelsize=18)
ax.tick_params(axis='y', labelsize=18)
ax.tick_params(axis='both', width=2)

# Thicken the border (spines)
for spine in ax.spines.values():
    spine.set_linewidth(2)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("ratio.pdf", format="pdf", dpi=800)
