from data_preprocess import data_preprocess
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
import pandas as pd

def feature_engineering():
    dataset = data_preprocess()
    dataset['Type'] = le.fit_transform(dataset['Type'])
    Target_0_count, Target_1_count = dataset['Target'].value_counts()
    Target_1 = dataset[dataset['Target'] == 1]
    Target_0 = dataset[dataset['Target'] == 0]
    Target_1_over = Target_1.sample(Target_0_count,replace=True)
    dataset_balanced = pd.concat([Target_1_over,Target_0], axis=0)
    dataset_balanced['Target'].groupby(dataset_balanced['Target']).count()
    data = dataset_balanced.copy()
    data = data.reset_index(drop=True)
    data.to_csv("machine_predictive_maintenance_clean_data.csv", index = False)
    return data

feature_engineering()
