import os 
import pandas as pd


data_path = os.path.join(os.path.dirname(__file__), 'crafted_data', 'ClassifiedFIKO.csv')

Test = pd.read_csv(data_path)

last_opened_program = Test['Opened Programs'].iloc[-1] 

# Filter the DataFrame for the specified "Opened Programs" value
filtered_df = Test[Test['Opened Programs'] == last_opened_program]

# Calculate the percentage of observations in Cluster 1
cluster_1_percentage = (filtered_df['Cluster'] == 1).sum() / len(filtered_df) * 100

# Print the result
print(f"[PLOT] The number of observations is  : { len(filtered_df):.2f}")

print(f"[PLOT] The percentage of fatigue per observations is  : {cluster_1_percentage:.2f}%")
