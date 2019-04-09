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

fig, ax = plt.subplots(figsize=(14,6))

# create boxplot
sns.boxplot(x="Year", 
y="Age", 
ax=ax, 
hue="Sex", 
palette={"Male": "#18a1cd", "Female":"#fa8c00"}, 
data=summer_df)
        
ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Age (in years)', size=14)
ax.set_title('Age distribution of Hungarian athletes in Summer Olympics', size=16, pad=20, weight='heavy')
plt.show()