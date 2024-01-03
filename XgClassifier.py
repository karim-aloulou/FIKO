import os
import xgboost as xgb
import pandas as pd



model_file_path = os.path.join(os.path.dirname(__file__), 'FIKO_notebook', 'xgFIKO_classifier.model')

data_path = os.path.join(os.path.dirname(__file__), 'crafted_data', 'plot_data.csv')



loaded_model = xgb.XGBClassifier(objective="binary:logistic")

loaded_model.load_model(model_file_path)
print('[Xgclassifier]: model loaded')

data = pd.read_csv(data_path)
print('[Xgclassifier]: data loaded')



data_new=data.drop(['Opened Programs','Frame Number'],axis=1)
data_pred=loaded_model.predict(data_new)

data['Cluster']=data_pred

print('[Xgclassifier]: clusters predicted')
csv_file_path = 'ClassifiedFIKO.csv'

# Use the to_csv method to save the DataFrame to a CSV file
data.to_csv('crafted_data/'+csv_file_path, index=False)
print('[Xgclassifier]: data saved')


