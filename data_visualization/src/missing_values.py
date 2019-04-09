# inspiration from https://www.kaggle.com/goldendime/advanced-techniques-for-dealing-w-missing-data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loadData import preProcess, filterColumn

# Load and preprocess data 
hun_df = preProcess('./data/athlete_events.csv')
# select Summer Games only
hun_df = filterColumn(hun_df, 'Season', 'Summer')
# select a subset of the dataframe and drop duplicate ID from the same year
hun_df = hun_df[['Year', 'ID', 'Height','Weight', 'Age', 'Sex']].drop_duplicates(['Year', 'ID']).reset_index(drop=True)

# get the value counts for Height, Weight and Age values grouped by year
grouped_df = hun_df.groupby('Year')[['Height', 'Weight', 'Age']].count()

# calculate the number of athletes for each Game and add the result to a column named Total
number_of_athletes = hun_df['Year'].value_counts().sort_index()
grouped_df['Total'] = number_of_athletes.values

#grouped_df.to_csv('./data/missing_values.csv')

fig, ax = plt.subplots(figsize=(8,3))
grouped_df[['Height', 'Weight', 'Age', 'Total']].plot(ax=ax, linewidth=1.5)

ax.legend(bbox_to_anchor=(1.0, 1.0), frameon=False)
ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Number of records', size=14, labelpad=10)
#ax.set_title('Number of height, weight and age data points per year vs \ntotal number of records per year', pad=20, weight='heavy')

plt.tight_layout()
plt.show()