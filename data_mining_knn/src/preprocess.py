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
    # adult_deduplicated.drop('fnlwgt', axis=1, inplace=True)

    return train_dataset_clean, test_dataset_clean

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
    Args:
        X_train: Training features as Pandas DataFrame
        y_train: Training labels as Pandas Series
        X_test: Testing features as Pandas DataFrame
        y_test: Testing labels as Pandas Series
    Returns:
        X_train: One hot encoded training features as Pandas DataFrame.
        y_train: One hot encoded training labels as Pandas Series.
        X_test: One hot encoded testing features as Pandas DataFrame.
        y_test: One hot encoded testing labels as Pandas Series.
    
    """
    data = pd.concat([X_train, X_test])
    data_ohe = pd.get_dummies(data)
    X_train_ohe = data_ohe[:len(X_train)]
    X_test_ohe = data_ohe[len(X_train):]
    X_train_ohe.reset_index(drop=True)

    # earns column: 0 for '<=50K', 1 for '>50K'
    y_train_ohe = y_train.map({'<=50K': 0, '>50K': 1}).astype(int).reset_index(drop=True)
    y_test_ohe = y_test.map({'<=50K': 0, '>50K': 1}).astype(int).reset_index(drop=True)
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