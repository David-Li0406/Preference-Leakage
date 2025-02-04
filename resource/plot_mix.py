import matplotlib.pyplot as plt

# Data
x = [10, 30, 50, 70, 100]
alpacaeval_human = [3.6, 6.9, 8.3, 12.4, 18.4]
arenahard_human = [12.1,13.6,22.0,24.8,28.7]

alpacaeval_syn = [-0.8, 3.1, 8.1, 9.6, 18.4]
arenahard_syn = [0.5, 4.1, 13.7, 16.9, 28.7]

# Plot
plt.figure(figsize=(8, 6))
plt.plot(x, alpacaeval_human, marker='o', color="#2770B3", label='AlpacaEval2.0 - Manual', linewidth=2, markersize=8)
plt.plot(x, arenahard_human, marker='x', color="#EB661E", label='ArenaHard - Manual', linewidth=2, markersize=8)
plt.plot(x, alpacaeval_syn, marker='*', color="#2770B3", linestyle="--", label='AlpacaEval2.0 - Synthetic', linewidth=2, markersize=8)
plt.plot(x, arenahard_syn, marker='+', color="#EB661E",  linestyle="--", label='ArenaHard - Synthetic', linewidth=2, markersize=8)

# Labels and title
plt.xlabel('Contamination Ratio (%)', fontsize=16)
plt.ylabel('Preference Leakage Score (%)', fontsize=16)
plt.grid(True)
plt.legend(fontsize=16)

plt.tick_params(axis='x', labelsize=16)  # Set font size for x-axis tick labels
plt.tick_params(axis='y', labelsize=16)  # Set font size for y-axis tick labels

# Show the plot
plt.tight_layout()
plt.savefig("ratio.pdf", format="pdf", dpi=800)
