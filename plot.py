

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Make sure seaborn is imported for KDE plots
# Import seaborn as sns if you haven't already

# Set the path to your data file
data_path = os.path.join(os.path.dirname(__file__), 'crafted_data', 'plot_data.csv')

# Create a figure with 4 subplots outside the loop
fig, axs = plt.subplots(4, 1, figsize=(10, 8))

while True:
    df = pd.read_csv(data_path)

    last_opened_program = df['Opened Programs'].iloc[-1]

    # Filter the DataFrame for the specified "Opened Programs" value
    filtered_df = df[df['Opened Programs'] == last_opened_program]

    # Clear the axes for the new data
    for ax in axs:
        ax.clear()

    # Plot KDE on each subplot with different colors
    sns.kdeplot(filtered_df['Eye Aspect Ratio'], ax=axs[0], color='red', label='Eye Aspect Ratio')
    sns.kdeplot(filtered_df['Mouth Aspect Ratio'], ax=axs[1], color='blue', label='Mouth Aspect Ratio')
    sns.kdeplot(filtered_df['Head Tilt Degree'], ax=axs[2], color='green', label='Head Tilt Degree')
    sns.kdeplot(filtered_df['Eye Pupil'], ax=axs[3], color='purple', label='Eye Pupil')

    # Add labels and legends to each subplot
    for ax in axs:
        ax.set_xlabel('Value')
        ax.set_ylabel('Density')
        ax.legend()

    plt.tight_layout()
    plt.draw()
    plt.pause(3)

    # Check if the plot window is still open
    if not plt.get_fignums():
        break

# No need to clear the figure at the end of the loop
