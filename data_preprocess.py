from load_data import load_data

def data_preprocess():
    dataset = load_data()
    dataset.drop(['UDI','Product ID','Failure Type'], axis = 1, inplace = True)
    print(dataset.head())
    return dataset

data_preprocess()