import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype

def loadData(path):
    """
    Load the data into a Pandas DataFrame. 
    Args:
        path: String path to dataset.
    Returns:
        df: Data as a Pandas DataFrame.
    """
    df = pd.read_csv(path, index_col=0)
    return df

def filterColumn(df, column, condition):
    """
    Filter Pandas DataFrame based on condition
    Reset index
    Args:
        df: Pandas DataFrame
        column: the column we want to select from
        condition: selection will be based on this condition
    Returns:
        filterd_df: Filtered data as a Pandas DataFrame.
    """
    mask = df[column].values == condition
    filtered_df = df[mask]
    filtered_df.reset_index(drop=True, inplace=True)
    return filtered_df

def convertDataType(df):
    """
    Convert certain column data types to categorical
    Args:
        df: Dataset as a Pandas DataFrame.
    Returns:
        df: Data as a Pandas DataFrame, certain column data types converted to categorical
    """
    # set data type of Medal column as ordinal
    medal_cat = CategoricalDtype(ordered=True, categories=['No medal', 'Bronze', 'Silver', 'Gold'])
    df['Medal'] = df['Medal'].astype(medal_cat)

    # set data type of gender column as nominal
    gender_cat = CategoricalDtype(ordered=False, categories=['Male', 'Female'])
    df['Sex'] = df['Sex'].map({'M': 'Male', 'F': 'Female'}).astype(gender_cat)

    # set data type of Season column as nominal
    season_cat = CategoricalDtype(ordered=False, categories=['Summer', 'Winter'])
    df['Season'] = df['Season'].astype(season_cat)

    return df


def preProcess(path):
    """
    Load the data into a Pandas DataFrame. 
    Preprocess the data
    Args:
        path: String path to dataset.
    Returns:
        final_df: Data as a Pandas DataFrame.
    """
    df = loadData(path)
    # select Hungarian athletes only
    hun_df = filterColumn(df, 'NOC', 'HUN')
    # fill missing values in Medal column with No medal
    hun_df['Medal'].fillna('No medal', inplace = True)
    
    # drop Team column
    # Teams here refer to the country or the different athletic clubs that have participated in the Olympics. 
    # Since all athletes represent the same country (Hungary) in our dataset, 
    # I decided to drop the Team column, because it’s irrelevant.
    hun_df.drop('Team', axis=1, inplace=True)

    # remove 1906 Games and Art Competitions
    # the medals distributed at the 1906 Intercalated Games are not officially recognized by the IOC today
    # https://en.wikipedia.org/wiki/1906_Intercalated_Games

    final = hun_df.loc[(hun_df['Year'].values != 1906) & (hun_df['Sport'].values != 'Art Competitions')]
    # convert data type of certain columns to categorical
    final_df = convertDataType(final)
    final_df.reset_index(drop=True, inplace=True)

    return final_df

def filterMedalsOnly(df):
    """
    Filter Pandas DataFrame to contain records of athletes who have won a medal only
    Delete rows with no medal
    Reset index
    Args:
        df: Pandas DataFrame
    Returns:
        filterd_df: Filtered data as a Pandas DataFrame.
    """
    mask = df['Medal'].values != 'No medal'
    filtered_df = df[mask]
    filtered_df.reset_index(drop=True, inplace=True)
    return filtered_df
