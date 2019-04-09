import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loadData import preProcess

# Load and preprocess data 
hun_df = preProcess('./data/athlete_events.csv')

# select a subset of data
df = hun_df[['Games','Year', 'Season', 'ID']]

# create a hierarchical index
df.set_index(['Games', 'Year', 'Season'], inplace=True, append=True)

#group by year and season columns, keep unique values (ID) in each group
df_grouped = df.groupby(level=['Year', 'Season']).nunique()

# get a cross section of the dataframe for each season
summer = df_grouped.xs('Summer', level='Season')
winter = df_grouped.xs('Winter', level='Season')
fig, ax = plt.subplots(figsize=(9,6))
summer.plot(ax = ax,style='o-')
winter.plot(ax = ax,style='o-')

ax.legend(labels=['Summer', 'Winter'],bbox_to_anchor=(1.0, 1.0))
years = list(range(1896, 2022, 8))
plt.xticks(years)
ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Number of athletes', size=14, labelpad=10)
plt.title("Number of athletes representing Hungary in the Olympics", size=16, pad=20, weight='heavy')
plt.tight_layout()
plt.show()