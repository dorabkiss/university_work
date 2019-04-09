import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterColumn, filterMedalsOnly
from textwrap import wrap

# load data
hun_df = preProcess('./data/athlete_events.csv')
hun_df['Medal'] = hun_df['Medal'].astype('object')

# filter dataframe to contain rows with medals only, then select Summer Games only
filtered_df = filterMedalsOnly(hun_df)
filtered_df = filterColumn(filtered_df, 'Season', 'Summer')

# cross tabulate dataframe so that we get medal counts per athlete
medal_per_id = pd.crosstab(filtered_df['Name'], filtered_df['Medal'])

# reorder columns
top10 = medal_per_id[['Gold', 'Silver', 'Bronze']]

# create medal count column to store total number of medals for a sport
medal_per_id['Medal count'] = medal_per_id.sum(axis=1)

# sort by total count 
medal_per_id.sort_values('Medal count', ascending=False, inplace=True)

cols = ['#D4AF37', '#BCC6CC', '#cd7f32']

fig, ax = plt.subplots(figsize=(12,6))

# plot the number of gold, silver and bronze medals per sport as a stacked bar chart
medal_per_id[['Gold', 'Silver', 'Bronze']].iloc[0:10].plot.bar(ax=ax,
stacked=True, 
rot=0,
color=cols)

labels = medal_per_id.index.values
labels = ['\n'.join(wrap(l, 14)) for l in labels]
plt.setp(ax.set_xticklabels(labels))

# add title, x and y labels and grid lines
title = '''Hungary's\ most\ successful\ athletes'''
plt.title(r"$\bf{" + title + "}$" + '\n Medal counts for top 10 athletes, based on total count', size=16, pad=20)
ax.set_xlabel('Athlete', size=14, labelpad=10) 
ax.set_ylabel('Number of medals', size=14, labelpad=10)
ax.grid(which='major', axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()