import matplotlib.pyplot as plt
import numpy as np
import sys

# Check if file is provided as command line argument
if len(sys.argv) < 3:
    print("Usage: python visualization.py <data_file> <output_image>")
    sys.exit(1)

# Read the file passed as an argument
file_path = sys.argv[1]
output_image_path = sys.argv[2]

try:
    with open(file_path, 'r') as file:
        raw_data = file.read().split()  # Read file and split by spaces
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

# Convert data from file into percentages
data = [float(raw_data[i + 1].replace('%', '')) for i in range(0, len(raw_data), 2)]
labels = [raw_data[i] for i in range(0, len(raw_data), 2)]  # Store labels (numbers)

# Create a colormap that goes from 0% to 100%
cmap = plt.get_cmap('coolwarm')

# Split data into even and odd, and organize into two rows
even_data_top = [data[i] for i in range(0, 24, 2)]  # 0-22
even_data_bottom = [data[i] for i in range(24, 48, 2)]  # 24-46
even_labels_top = [labels[i] for i in range(0, 24, 2)]
even_labels_bottom = [labels[i] for i in range(24, 48, 2)]

odd_data_top = [data[i] for i in range(1, 24, 2)]  # 1-23
odd_data_bottom = [data[i] for i in range(25, 48, 2)]  # 25-47
odd_labels_top = [labels[i] for i in range(1, 24, 2)]
odd_labels_bottom = [labels[i] for i in range(25, 48, 2)]

# Plot settings
def plot_data(top_values, bottom_values, top_labels, bottom_labels, title, ax):
    colors_top = [cmap(val / 100) for val in top_values]  # normalize percentages for colormap (top row)
    colors_bottom = [cmap(val / 100) for val in bottom_values]  # normalize percentages for colormap (bottom row)

    ax.set_title(title)
    ax.set_xticks([])  # No axis ticks
    ax.set_yticks([])

    # Plot each number as a square (top row)
    for i, (val, label, color) in enumerate(zip(top_values, top_labels, colors_top)):
        ax.add_patch(plt.Rectangle((i % 12, 1), 1, 1, color=color))  # Y = 1 for top row
        ax.text(i % 12 + 0.5, 1.5, f"{label}\n{val}%", va='center', ha='center', color='black')

    # Plot each number as a square (bottom row)
    for i, (val, label, color) in enumerate(zip(bottom_values, bottom_labels, colors_bottom)):
        ax.add_patch(plt.Rectangle((i % 12, 0), 1, 1, color=color))  # Y = 0 for bottom row
        ax.text(i % 12 + 0.5, 0.5, f"{label}\n{val}%", va='center', ha='center', color='black')

    ax.set_xlim(0, 12)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')

# Create subplots for even and odd numbers
fig, axes = plt.subplots(1, 2, figsize=(14, 5))  # Increase the figure size

# Plot even data
plot_data(even_data_top, even_data_bottom, even_labels_top, even_labels_bottom, 'package 0', axes[0])

# Plot odd data
plot_data(odd_data_top, odd_data_bottom, odd_labels_top, odd_labels_bottom, 'package 1', axes[1])

# Adjust the layout to give more space
plt.tight_layout(pad=3.0)  # Increase padding
plt.subplots_adjust(top=0.85)  # Decrease the top margin to move plots up

# Add a colorbar (legend) with adjusted padding
cbar = fig.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=100)), ax=axes, orientation='horizontal', fraction=0.05, pad=0.25)
cbar.set_label('% Cstate(c6)')

# Save the figure as an image file
plt.savefig(output_image_path)
print(f"Image saved as {output_image_path}")