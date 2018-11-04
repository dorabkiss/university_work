import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.api.types import CategoricalDtype
import math

def loadData(train_path, test_path):
    """
    Load the data into a Pandas DataFrame. 
    Skip the first row (header) and name the columns uniformly for both datasets
    Args:
        train_path: String path to training dataset.
        test_path: String path to testing dataset.
    Returns:
        train_dataset: Training data as a Pandas DataFrame.
        test_dataset: Testing data as a Pandas DataFrame.
    """
    train_dataset = pd.read_csv(train_path, header = None, skiprows= 1, 
    names=['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 
    'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country',
    'earns', 'fold'])

    # remove whitespace by using regex in the sep parameter of read_csv. It also requires the argument engine="python"
    test_dataset = pd.read_csv(test_path, header = None, skiprows= 1, sep=' *, *', engine='python',
    names=['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 
    'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 
    'earns'])

    return train_dataset, test_dataset

def cleanData(train_dataset, test_dataset):
    """
    Clean the training and testing datasets by removing invalid and duplicate data points.
    Args:
        train_dataset: Train data as Pandas DataFrame.
        test_dataset: Test data as Pandas DataFrame.
    Returns:
        train_dataset_clean: Cleaned training data in Pandas DataFrame.
        test_dataset_clean: Cleaned testing data in Pandas DataFrame.
    """
    # Replace all "?" with NaN and then drop rows where NaN appears
    train_dataset_no_na = train_dataset.replace('?', np.NaN).dropna()
    test_dataset_no_na = test_dataset.replace('?', np.NaN).dropna()

    # remove duplicates. Use copy() to avoid SettingWithCopyWarning. 
    # (If we modify values in df later we will find that the modifications do not propagate back to the 
    # original data (df), and that Pandas does warning)
    train_dataset_deduplicated = train_dataset_no_na.drop_duplicates().copy()
    test_dataset_deduplicated = test_dataset_no_na.drop_duplicates().copy()

    # education and education_num columns represent the same features, but encoded as strings and as numbers. 
    # We don’t need the string representation, so we can just delete the education column.
    # fold is an auxiliary column and should not be used as a predictor, 
    # but just to indicate the fold that you must use in the 5-Cross Validation (denoted 5CV) for model optimisation. 
    train_dataset_clean = train_dataset_deduplicated.drop(['education', 'fold'], axis=1)
    test_dataset_clean = test_dataset_deduplicated.drop('education', axis=1)

    #TODO We also Ignore the column fnlwgt, as it just adjusts for population, and has almost no predictive power.
    # Capital_gain has 102 unique values. Out of 10201 records 9350 have 0 values (91.7%). 
    # Capital gain has 96% instances with zero values for less than 50K (7349 out of total 7664) 
    # and 79% instances with zero values for >50K (2001/2537). 

    # Capital loss each has 78 unique values. Out of 10201 records 9713 have zero values (95.2%)
    # Capital loss has 97% instances with zero values for less than 50K (7427 out of total 7664)
    # and 90% instances with zero values for >50K (2286/2537). 
    
    # This implies that capital gain or loss will not make significant predictors either.
    # it might be useful to remove them during feature selection.

    # adult_deduplicated.drop('capital_gain', axis=1, inplace=True)
    # adult_deduplicated.drop('capital_loss', axis=1, inplace=True)

    # remove less significant columns
    # fnlwgt
    # adult_deduplicated.drop('fnlwgt', axis=1, inplace=True)

    return train_dataset_clean, test_dataset_clean

def transformData(train_dataset, test_dataset):
    """
    Rearrange the training and testing data to make them more simple and meaningful 
    by reducing the number of categories for nominal variables.
    Args:
        train_dataset: Train data as Pandas DataFrame.
        test_dataset: Test data as Pandas DataFrame.
    Returns:
        train_dataset: Transformed training data in Pandas DataFrame.
        test_dataset: Transformed testing data in Pandas DataFrame.
    """
    # copy and modify that dataset or just call functions on input dataset?
    #result_train = train_dataset.copy()
    #result_test = test_dataset.copy()

    # some data are too detailed, like 'marital-status' and ‘native_country’.
    # this function modifies the input datasets!

    # where relationship is 'Husband' or 'Wife', change it to 'Married'
    train_dataset.loc[((train_dataset['relationship'] == 'Husband') | (train_dataset['relationship'] == 'Wife')) , "relationship"] = 'Married'
    test_dataset.loc[((test_dataset['relationship'] == 'Husband') | (test_dataset['relationship'] == 'Wife')) , "relationship"] = 'Married'
    
    # where marital_status is 'Married-*', change it to 'Married'
    train_dataset.loc[((train_dataset['marital_status'] == 'Married-civ-spouse') | (train_dataset['marital_status'] == 'Married-AF-spouse') | (train_dataset['marital_status'] == 'Married-spouse-absent')) , "marital_status"] = 'Married'
    test_dataset.loc[((test_dataset['marital_status'] == 'Married-civ-spouse') | (test_dataset['marital_status'] == 'Married-AF-spouse') | (test_dataset['marital_status'] == 'Married-spouse-absent')) , "marital_status"] = 'Married'

    # where marital_status is 'Divorced' or 'Never-married' or 'Separated' or 'Widowed', change it to 'Unmarried'
    train_dataset.loc[((train_dataset['marital_status'] == 'Divorced') | (train_dataset['marital_status'] == 'Never-married') | (train_dataset['marital_status'] == 'Separated') | (train_dataset['marital_status'] == 'Widowed')) , "marital_status"] = 'Unmarried'
    test_dataset.loc[((test_dataset['marital_status'] == 'Divorced') | (test_dataset['marital_status'] == 'Never-married') | (test_dataset['marital_status'] == 'Separated') | (test_dataset['marital_status'] == 'Widowed')) , "marital_status"] = 'Unmarried'

    # native_country column: group the countries by global regions
    # assuming that 'South' stands for South Korea and 'Hong' for Hong Kong
    train_dataset['native_country'] = train_dataset['native_country'].map({'United-States': 'North_America', 'Mexico': 'North_America', 'Philippines': 'Asia', 'Germany': 'Europe', 'Canada': 'North_America', 'Puerto-Rico': 'Central_America', 'Jamaica': 'Central_America', 'India': 'Asia', 'South': 'Asia', 'China': 'Asia', 'El-Salvador': 'Central_America', 'Dominican-Republic': 'Central_America', 'England': 'Europe', 'Poland': 'Europe', 'Columbia': 'South_America', 'Cuba': 'Central_America', 'Italy': 'Europe', 'Japan': 'Asia', 'Vietnam': 'Asia', 'Guatemala': 'Central_America', 'Iran': 'Asia', 'France': 'Europe', 'Nicaragua': 'Central_America', 'Peru': 'South_America', 'Taiwan': 'Asia', 'Greece': 'Europe', 'Ireland': 'Europe', 'Ecuador': 'South_America', 'Haiti': 'Central_America', 'Cambodia': 'Asia', 'Hong': 'Asia', 'Portugal': 'Europe', 'Trinadad&Tobago': 'Central_America', 'Thailand': "Asia", 'Yugoslavia': 'Europe', 'Honduras': 'Central_America', 'Laos': 'Asia', 'Hungary': 'Europe', 'Scotland': 'Europe', 'Holand-Netherlands': 'Europe', 'Outlying-US(Guam-USVI-etc)': 'North_America'})
    test_dataset['native_country'] = test_dataset['native_country'].map({'United-States': 'North_America', 'Mexico': 'North_America', 'Philippines': 'Asia', 'Germany': 'Europe', 'Canada': 'North_America', 'Puerto-Rico': 'Central_America', 'Jamaica': 'Central_America', 'India': 'Asia', 'South': 'Asia', 'China': 'Asia', 'El-Salvador': 'Central_America', 'Dominican-Republic': 'Central_America', 'England': 'Europe', 'Poland': 'Europe', 'Columbia': 'South_America', 'Cuba': 'Central_America', 'Italy': 'Europe', 'Japan': 'Asia', 'Vietnam': 'Asia', 'Guatemala': 'Central_America', 'Iran': 'Asia', 'France': 'Europe', 'Nicaragua': 'Central_America', 'Peru': 'South_America', 'Taiwan': 'Asia', 'Greece': 'Europe', 'Ireland': 'Europe', 'Ecuador': 'South_America', 'Haiti': 'Central_America', 'Cambodia': 'Asia', 'Hong': 'Asia', 'Portugal': 'Europe', 'Trinadad&Tobago': 'Central_America', 'Thailand': "Asia", 'Yugoslavia': 'Europe', 'Honduras': 'Central_America', 'Laos': 'Asia', 'Hungary': 'Europe', 'Scotland': 'Europe', 'Holand-Netherlands': 'Europe', 'Outlying-US(Guam-USVI-etc)': 'North_America'})

    #TODO
    # workclass: to reduce the number of categories, collapse local-gov, state-gov and federal-gov to gov
    #train_dataset['workclass'] = train_dataset['workclass'].map({'Private': 0, 'Self-emp-not-inc': 1, 'Local-gov': 'gov', 'State-gov': 'gov', 'Self-emp-inc': 4, 'Federal-gov': 'gov', 'Without-pay': 6})
    

    return train_dataset, test_dataset

def encodeCategoricalData(train_dataset, test_dataset):
    """
    Convert categorical data into numeric. KNN cannot work with strings.
    Args:
        train_dataset: Train dataset as Pandas DataFrame.
        test_dataset: Test dataset as Pandas DataFrame.
    Returns:
        train_dataset: Cleaned training data in Pandas DataFrame.
        test_dataset: Cleaned testing data in Pandas DataFrame.
    """  
    # workclass volumn: 0 for 'Private', 1 for 'Self-emp-not-inc', 2 for 'Local-gov', 3 for 'State-gov', 4 for 'Self-emp-inc', 5 for 'Federal-gov', 6 for 'Without-pay'  
    train_dataset['workclass'] = train_dataset['workclass'].map({'Private': 0, 'Self-emp-not-inc': 1, 'Local-gov': 2, 'State-gov': 3, 'Self-emp-inc': 4, 'Federal-gov': 5, 'Without-pay': 6}).astype(int)
    test_dataset['workclass'] = test_dataset['workclass'].map({'Private': 0, 'Self-emp-not-inc': 1, 'Local-gov': 2, 'State-gov': 3, 'Self-emp-inc': 4, 'Federal-gov': 5, 'Without-pay': 6}).astype(int)

    # marital_status column: 0 for 'Married', 1 for 'Unmarried'
    train_dataset['marital_status'] = train_dataset['marital_status'].map({'Married': 0, 'Unmarried': 1}).astype(int)
    test_dataset['marital_status'] = test_dataset['marital_status'].map({'Married': 0, 'Unmarried': 1}).astype(int)
    
    # TODO occupation

    # relationship: 0 for 'Married', 1 for 'Unmarried', 2 for 'Not-in-family', 3 for 'Own-child', 4 for 'Other-relative'
    train_dataset['relationship'] = train_dataset['relationship'].map({'Married': 0, 'Unmarried': 1, 'Not-in-family': 2, 'Own-child': 3, 'Other-relative': 4}).astype(int)
    test_dataset['relationship'] = test_dataset['relationship'].map({'Married': 0, 'Unmarried': 1, 'Not-in-family': 2, 'Own-child': 3, 'Other-relative': 4}).astype(int)

    # race column: 0 for 'White', 1 for 'Black', 2 for 'Asian-Pac-Islander', 3 for 'Amer-Indian-Eskimo', 4 for 'Other'
    train_dataset['race'] = train_dataset['race'].map({'White': 0, 'Black': 1, 'Asian-Pac-Islander': 2, 'Amer-Indian-Eskimo': 3, 'Other': 4}).astype(int)
    test_dataset['race'] = test_dataset['race'].map({'White': 0, 'Black': 1, 'Asian-Pac-Islander': 2, 'Amer-Indian-Eskimo': 3, 'Other': 4}).astype(int)

    # sex column: 0 for 'Female', 1 for 'Male'
    train_dataset['sex'] = train_dataset['sex'].map({'Female': 0, 'Male': 1}).astype(int)
    test_dataset['sex'] = test_dataset['sex'].map({'Female': 0, 'Male': 1}).astype(int)
    
    # native_country: 0 for 'North_America', 1 for 'Asia', 2 for 'Central_America', 3 for 'Europe', 4 for 'South_America'
    train_dataset['native_country'] = train_dataset['native_country'].map({'North_America': 0, 'Asia': 1, 'Central_America': 2, 'Europe': 3, 'South_America': 4}).astype(int)
    test_dataset['native_country'] = test_dataset['native_country'].map({'North_America': 0, 'Asia': 1, 'Central_America': 2, 'Europe': 3, 'South_America': 4}).astype(int)

    # earns column: 0 for '<=50K', 1 for '>50K'
    train_dataset['earns'] = train_dataset['earns'].map({'<=50K': 0, '>50K': 1}).astype(int)
    test_dataset['earns'] = test_dataset['earns'].map({'<=50K': 0, '>50K': 1}).astype(int)

    return train_dataset, test_dataset

def encodeCategoricalData2(train_ds):
    """
    Convert categorical data into numeric. KNN cannot work with strings.
    Args:
        train_dataset: Train dataset as Pandas DataFrame.
        test_dataset: Test dataset as Pandas DataFrame.
    Returns:
        train_dataset: Cleaned training data in Pandas DataFrame.
        test_dataset: Cleaned testing data in Pandas DataFrame.
    """     
    # convert 'object' columns to a 'category', then use those category values for label encoding.
    # Then assign the encoded variable to a new column using the cat.codes accessor:
    for column in train_ds.columns:
        if train_ds.dtypes[column] == np.object:
            train_ds[column] = train_ds[column].astype('category')
            train_ds[column] = train_ds[column].cat.codes
    return train_ds

def normalize(df):
    """
    Normalize dataset to give equal weight to each feature.
    Args:
        train_dataset: Train dataset as Pandas DataFrame.
        test_dataset: Test dataset as Pandas DataFrame.
    Returns:
        train_dataset: Cleaned training data in Pandas DataFrame.
        test_dataset: Cleaned testing data in Pandas DataFrame.
    """ 
    result = df.copy()
    for column in df.columns:
        # skip columns that contain non-numeric data
        if (df.dtypes[column] == np.object):
            continue
        max_value = df[column].max()
        min_value = df[column].min()
        result[column] = (df[column] - min_value) / (max_value - min_value)
    return result

def split_data(train_data, test_data):
    """
    Split data into training/testing features and training/testing labels.
    Args:
        train_data: Train dataset as Pandas DataFrame.
        test_data: Test dataset as Pandas DataFrame.
    Returns:
        X_train: Train features as Pandas DataFrame.
        y_train: Train labels as Pandas Series.
        X_test: Test features as Pandas DataFrame.
        y_test: Test labels as Pandas Series.
    """ 
    y_train = train_data['earns']
    X_train = train_data.drop(['earns'], axis=1)

    y_test = test_data['earns']
    X_test = test_data.drop('earns', axis=1)

    return X_train, y_train, X_test, y_test

def ohe_data(X_train, y_train, X_test, y_test):
    """
    One hot encode categorical columns.
    
    """
    data = pd.concat([X_train, X_test])
    data_ohe = pd.get_dummies(data)
    X_train_ohe = data_ohe[:len(X_train)]
    X_test_ohe = data_ohe[len(X_train):]

    # earns column: 0 for '<=50K', 1 for '>50K'
    y_train_ohe = y_train.map({'<=50K': 0, '>50K': 1}).astype(int)
    y_test_ohe = y_test.map({'<=50K': 0, '>50K': 1}).astype(int)
    # or we can use replace instead of map
    # y_train_ohe = y_train.replace([' <=50K', ' >50K'], [0, 1])
    # y_test_ohe = y_test.replace([' <=50K', ' >50K'], [0, 1])

    return X_train_ohe, y_train_ohe, X_test_ohe, y_test_ohe

# another version for ohe
def oneHotEncode(df):
    """
    One hot encode categorical columns.
    Args:
        df: Pandas DataFrame.
    Returns:
        df: Pandas DataFrame, with categorical columns one hot encoded
    """ 
    obj_df = df.select_dtypes(include=['object'])
    return pd.get_dummies(df, columns=obj_df.columns).values