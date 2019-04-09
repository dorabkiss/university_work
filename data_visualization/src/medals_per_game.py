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

# cross tabulate dataframe so that we get medal counts for each Summer Olympics
medal_per_game = pd.crosstab(filtered_df['Year'], filtered_df['Medal'])

# reorder columns
medal_per_game = medal_per_game[['Gold', 'Silver', 'Bronze']]

cols = ['#D4AF37', '#BCC6CC', '#cd7f32']

fig, ax = plt.subplots(figsize=(9,6))

# plot the number of gold, silver and bronze medals per Olympic Game as a stacked bar chart
medal_per_game[['Gold', 'Silver', 'Bronze']].plot.bar(ax=ax,
stacked=True, 
color=cols)

# add title, x and y labels and grid lines
plt.title('Number of medals won by Hungary in the Summer Olympics', size=16, pad=20, weight='heavy')
ax.set_xlabel('Year', size=14, labelpad=10) 
ax.set_ylabel('Number of medals', size=14, labelpad=10)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()