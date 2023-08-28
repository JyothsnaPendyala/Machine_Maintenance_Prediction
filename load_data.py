import pandas as pd

def load_data():
    data = pd.read_csv("predictive_maintenance.csv")
    return data

load_data()