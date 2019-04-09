import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterColumn, filterMedalsOnly

# load data
hun_df = preProcess('./data/athlete_events.csv')
hun_df['Medal'] = hun_df['Medal'].astype('object')

# filter dataframe to contain rows with medals only, then select Summer Games only
filtered_df = filterMedalsOnly(hun_df)
filtered_df = filterColumn(filtered_df, 'Season', 'Summer')

# count medals for team sports as 1 
# (if we have more than 1 medal for one event in the same Olympic Game, it must be a team sport)
filtered_df = filtered_df.drop_duplicates(['Games', 'Event', 'Medal']).reset_index(drop=True)

# cross tabulate dataframe so that we get medal counts for each sport
medal_per_sport = pd.crosstab(filtered_df['Sport'], filtered_df['Medal'])

# reorder columns
top10 = medal_per_sport[['Gold', 'Silver', 'Bronze']]

# create medal count column to store total number of medals for a sport
medal_per_sport['Medal count'] = medal_per_sport.sum(axis=1)

# sort by total count 
medal_per_sport.sort_values('Medal count', ascending=False, inplace=True)
cols = ['#D4AF37', '#BCC6CC', '#cd7f32']

fig, ax = plt.subplots(figsize=(9,6))

# plot the number of gold, silver and bronze medals per sport as a stacked bar chart
medal_per_sport[['Gold', 'Silver', 'Bronze']].iloc[0:10].plot.bar(ax=ax,
stacked=True, 
color=cols)

# add title, x and y labels and grid lines
title = 'Sports\ with\ the\ greatest\ number\ of\ medals'
plt.title(r"$\bf{" + title + "}$" + '\n Medal counts for top 10 sports, based on total count', size=16, pad=20)
ax.set_xlabel('Sport', size=14, labelpad=10) 
ax.set_ylabel('Number of medals', size=14, labelpad=10)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()