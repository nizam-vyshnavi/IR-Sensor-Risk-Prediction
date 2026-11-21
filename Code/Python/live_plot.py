import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import numpy as np
import matplotlib.patches as mpatches
import random

# File paths
OUTPUT_FILE = 'C:/BNN_FINAL/output.txt'
INPUT_FILE = 'C:/BNN_FINAL/input.txt'

labels = ['Class 0', 'Class 1', 'Class 2', 'Class 3', 'Class 4']

# Read IR input values just once
def read_input_values_once():
    if not os.path.exists(INPUT_FILE):
        return []
    with open(INPUT_FILE, 'r') as f:
        try:
            return [int(x) for x in f.readline().strip().split()]
        except:
            return []

def read_predictions():
    if not os.path.exists(OUTPUT_FILE):
        return [0] * 5
    with open(OUTPUT_FILE, 'r') as f:
        try:
            return [int(x) for x in f.readline().strip().split()]
        except:
            return [0] * 5

def get_color(v):
    if v >= 90:
        return 'red'
    elif v > 10:
        return 'yellow'
    else:
        return 'green'

# Freeze the input values at start
frozen_inputs = read_input_values_once()
frozen_input_text = (
    "Mapped IR values (used in prediction): " + ' '.join(str(v) for v in frozen_inputs)
    if frozen_inputs else "Mapped IR values: N/A"
)

def update(frame):
    base_values = read_predictions()

    if len(base_values) != 5:
        base_values = [0] * 5

    # Add small ±3% random variation to simulate uncertainty
    varied_values = [min(100, max(0, v + random.randint(-3, 3))) for v in base_values]

    for i in range(5):
        bars[i].set_height(varied_values[i])
        bars[i].set_color(get_color(varied_values[i]))
        text_labels[i].set_text(f"{varied_values[i]}%")
        text_labels[i].set_y(varied_values[i] + 2)

# Initialize plot
fig, ax = plt.subplots()
x = np.arange(5)
bars = ax.bar(x, [0]*5, color='gray', edgecolor='black')
text_labels = [ax.text(i, 2, "0%", ha='center', fontsize=10) for i in x]

ax.set_ylim(0, 120)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Risk Confidence (%)")
ax.set_title("Real-Time Risk Prediction Visualization")

# Legend
red_patch = mpatches.Patch(color='red', label='High Risk (≥90%)')
yellow_patch = mpatches.Patch(color='yellow', label='Moderate Risk (11–89%)')
green_patch = mpatches.Patch(color='green', label='Low Risk (≤10%)')
ax.legend(handles=[green_patch, yellow_patch, red_patch], loc='upper right')

# Display fixed IR sensor input set
ax.text(0.5, 1.05, frozen_input_text, ha='center', va='bottom', transform=ax.transAxes,
        fontsize=9, bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

# Animation loop
ani = animation.FuncAnimation(fig, update, interval=1000, cache_frame_data=False)
plt.tight_layout()
plt.show()
