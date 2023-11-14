import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a pandas DataFrame
csv_file_path = 'plot_data.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file_path)

# Get the number of the open program as input
program_number = int(input("Enter the number of the open program: "))

# Filter the DataFrame based on the program number
program_df = df[df['Opened Programs'] == program_number]

# Plotting histograms, kernel density estimate, and boxplots for each feature
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Plot histogram and kernel density estimate for Eye Aspect Ratio
sns.histplot(program_df['Eye Aspect Ratio'], bins=20, kde=True, color='blue', ax=axes[0, 0])
axes[0, 0].set_title('Eye Aspect Ratio')

# Plot histogram and kernel density estimate for Mouth Aspect Ratio
sns.histplot(program_df['Mouth Aspect Ratio'], bins=20, kde=True, color='green', ax=axes[0, 1])
axes[0, 1].set_title('Mouth Aspect Ratio')

# Plot histogram and kernel density estimate for Head Tilt Degree
sns.histplot(program_df['Head Tilt Degree'], bins=20, kde=True, color='red', ax=axes[1, 0])
axes[1, 0].set_title('Head Tilt Degree')

# Plot histogram and kernel density estimate for Eye Pupil
sns.histplot(program_df['Eye Pupil'], bins=20, kde=True, color='cyan', ax=axes[1, 1])
axes[1, 1].set_title('Eye Pupil')

# Set common labels and show the plot
for ax in axes.flat:
    ax.set(xlabel='Value', ylabel='Frequency')

plt.tight_layout()

# Add boxplots below histograms
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# Boxplot for Eye Aspect Ratio
sns.boxplot(x=program_df['Eye Aspect Ratio'], ax=axes[0, 0], color='blue')
axes[0, 0].set_title('Eye Aspect Ratio')

# Boxplot for Mouth Aspect Ratio
sns.boxplot(x=program_df['Mouth Aspect Ratio'], ax=axes[0, 1], color='green')
axes[0, 1].set_title('Mouth Aspect Ratio')

# Boxplot for Head Tilt Degree
sns.boxplot(x=program_df['Head Tilt Degree'], ax=axes[1, 0], color='red')
axes[1, 0].set_title('Head Tilt Degree')

# Boxplot for Eye Pupil
sns.boxplot(x=program_df['Eye Pupil'], ax=axes[1, 1], color='cyan')
axes[1, 1].set_title('Eye Pupil')

# Set common labels and show the plot
for ax in axes.flat:
    ax.set(xlabel='Value', ylabel='')

plt.tight_layout()
plt.show()
