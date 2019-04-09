import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterColumn

# load data 
hun_df = preProcess('./data/athlete_events.csv')

# select summer games only
summer_df = filterColumn(hun_df, 'Season', 'Summer')
# select Games from 1960 onwards, because there are too many missing height/weight values for previous Olympics
summer_df = summer_df.loc[summer_df['Year'] > 1959]
fig, ax = plt.subplots(figsize=(20,6))

# create boxplot
a = sns.boxplot(x="Year", y="Height", ax=ax, hue="Sex", 
palette={"Male": "#18a1cd", "Female":"#fa8c00"}, 
data=summer_df)
        
ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Height (cm)', size=14, labelpad=10)
ax.set_title('Height distribution of Hungarian atheletes in Summer Olympic games 1960-2016', size=16, pad=20, weight='heavy')
plt.show()