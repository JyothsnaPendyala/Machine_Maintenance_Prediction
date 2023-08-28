from data_preprocess import data_preprocess
import matplotlib.pyplot as plt
import seaborn as sns

def data_visualisation():
    dataset = data_preprocess()
    categorical_features = ['Type','Target']
    numerical_features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]','Tool wear [min]']

    # distribution plots
    for numerical_feature in numerical_features:
        plt.subplots(1,1, figsize=(5,5))
        sns.distplot(x = dataset[numerical_feature])
        plt.xlabel(numerical_feature)
        plt.title(numerical_feature)
    plt.show()

    # count plots
    for categorical_feature in categorical_features:
        sns.countplot(x=categorical_feature,data=dataset)
        plt.xlabel(categorical_feature)
        plt.title(categorical_feature)
    plt.show()
    
    # Box plots
    for numerical_feature in numerical_features:
        plt.subplots(1,1, figsize=(5,5))
        sns.boxplot(x = dataset[numerical_feature])
        plt.xlabel(numerical_feature)
        plt.title(numerical_feature)
        plt.show()
    
    # pair plots
    sns.pairplot(dataset , hue = 'Target')
    plt.show() 

    # correlation matrix
    # cor_mat = dataset.corr()
    # fig = plt.figure(figsize=(12,7))
    # sns.heatmap(cor_mat,annot=True)
    # plt.show()
    
    return dataset

data_visualisation()
