import xgboost as xgb
import pandas as pd
import os
model_file_path = os.path.join(os.path.dirname(__file__), 'FIKO_notebook', 'xgFIKO_classifier.model')

data_path = os.path.join(os.path.dirname(__file__), 'crafted_data', 'plot_data.csv')

# def remove_outliers(data,X):
#     column_data = data[X]
#     Q1 = column_data.quantile(0.25)
#     Q3 = column_data.quantile(0.75)
#     IQR = Q3 - Q1

#     # Step 3: Define the lower and upper bounds to identify outliers
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR

#     # Step 4: Identify and remove outliers from the DataFrame
#     outliers = data[(column_data < lower_bound) | (column_data > upper_bound)]
#     data = data[(column_data >= lower_bound) & (column_data <= upper_bound)]
#     return data

loaded_model = xgb.XGBClassifier(objective="binary:logistic")

loaded_model.load_model(model_file_path)
print('[Xgclassifier]: model loaded')

data = pd.read_csv(data_path)
print('[Xgclassifier]: data loaded')

# data=remove_outliers(data,'Eye Aspect Ratio')
# data=remove_outliers(data,'Mouth Aspect Ratio')
# data=remove_outliers(data,'Head Tilt Degree')
# data=remove_outliers(data,'Eye Pupil')
# print('[Xgclassifier]: outliers removed')

data_new=data.drop(['Opened Programs','Frame Number'],axis=1)
data_pred=loaded_model.predict(data_new)

data['Cluster']=data_pred

print('[Xgclassifier]: clusters predicted')
csv_file_path = 'ClassifiedFIKO.csv'

# Use the to_csv method to save the DataFrame to a CSV file
data.to_csv('crafted_data/'+csv_file_path, index=False)
print('[Xgclassifier]: data saved')


