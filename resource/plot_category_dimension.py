import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Data from the OCR
categories = ["Completeness", "Clarity", "Richness", "Satisfaction", "Factuality", "Logical", "Others", "Creativity", "Fairness"]
scores = [27.9, 28.6, 28.8, 29.0, 29.2, 30.2, 30.4, 30.7, 32.4]

# Paths to icons (replace with actual file paths)
icon_paths = [
    "icons/completeness.png",
    "icons/clarity.png",
    "icons/richness.png",
    "icons/satisfaction.png",
    "icons/factuality.png",
    "icons/logical.png",
    "icons/others.png",
    "icons/creativity.png",
    "icons/fairness.png"
]

# Create the bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
bars = plt.bar(categories, scores, color='#9AB7F1')  # Set bar color

# Add labels and title
plt.ylabel('Preference Leakage Score (%)', fontsize=20)
plt.xticks(rotation=45, ha='right', fontsize=20)  # Rotate x-axis labels for readability
plt.yticks(fontsize=20)  # Adjust y-axis ticks size
plt.ylim(20, 34)
plt.yticks([20, 24, 28, 32])

# Add score labels above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 1), ha='center', va='bottom', fontsize=18)

# Add icons below each bar
ax = plt.gca()
for bar, icon_path in zip(bars, icon_paths):
    xval = bar.get_x() + bar.get_width() / 2
    yval = 21  # Adjust to position the icon below the x-axis
    img = plt.imread(icon_path)
    imagebox = OffsetImage(img, zoom=0.08)  # Adjust zoom for icon size
    ab = AnnotationBbox(imagebox, (xval, yval), frameon=False, xycoords='data')
    ax.add_artist(ab)

# Add grid
plt.grid(axis='y', linestyle='--')
# plt.tight_layout()
plt.subplots_adjust(bottom=0.27, top=0.99)

# Save the plot
plt.savefig("category_dimension.pdf", format="pdf", dpi=800)