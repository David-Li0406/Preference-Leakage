import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Data from the OCR
categories = ['Mathematics', 'Business', 'Daily Life', 'Science', 'Writing', 'Others', 'Programming']
scores = [7.7, 16.5, 17.2, 17.3, 21.0, 23.8, 31.4]

# Icons for each category (replace with paths to your actual images)
icon_paths = [
    "icons/math.png",        # Mathematics
    "icons/business.png",    # Business
    "icons/daily_life.png",  # Daily Life
    "icons/science.png",     # Science
    "icons/writing.png",     # Writing
    "icons/others.png",      # Others
    "icons/programming.png"  # Programming
]

# Create the bar chart
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
bars = plt.bar(categories, scores, color='#FFA400')  # set bar color

# Add labels and title
plt.ylabel('Preference Leakage Score (%)', fontsize=20)
plt.xticks(rotation=45, ha='right', fontsize=20)  # Rotate x-axis labels for readability
plt.yticks(fontsize=20)  # Adjust y-axis ticks size
plt.ylim(0, 34)
plt.yticks([0, 10, 20, 30])

# Add score labels above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 1), ha='center', va='bottom', fontsize=18)

# Add icons below each bar
for bar, icon_path in zip(bars, icon_paths):
    xval = bar.get_x() + bar.get_width() / 2
    yval = 2.7  # Adjust to position the icon below the x-axis
    img = plt.imread(icon_path)
    imagebox = OffsetImage(img, zoom=0.085)  # Adjust zoom for icon size
    ab = AnnotationBbox(imagebox, (xval, yval), frameon=False, xycoords='data')
    plt.gca().add_artist(ab)

# Add grid
plt.grid(axis='y', linestyle='--')
# plt.tight_layout()
plt.subplots_adjust(bottom=0.26, top=0.99)

# Show the plot
plt.savefig("category_data.pdf", format="pdf", dpi=800)
