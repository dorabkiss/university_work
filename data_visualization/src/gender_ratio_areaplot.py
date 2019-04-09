import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterColumn

df = preProcess('./data/athlete_events.csv')

# drop duplicate ID from the same Games
df = df.drop_duplicates(['Games', 'ID'])

# select summer games only
df_summer = filterColumn(df, 'Season', 'Summer')

# get the number of female and male athletes (no duplicates) per summer game and normalize values
gender_ratio_per_year = pd.crosstab([df_summer['Year']], df_summer['Sex']).apply(lambda r: r/r.sum(), axis=1)

cols = ['#18a1cd', '#fa8c00']

ax = gender_ratio_per_year.plot.area(stacked=True, figsize=(12,6), color=cols)
handles, labels = ax.get_legend_handles_labels()

# create legend
ax.legend(handles, labels, bbox_to_anchor=(1.0, 1.0), frameon=False)

# add title, x and y labels, x ticks
plt.title('Gender ratio of Hungarian athletes in the Summer Olympics over time', size=16, pad=20, weight='heavy')
ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Ratio', size=14, labelpad=10) 
years = list(range(1896, 2022, 8))
plt.xticks(years)

plt.tight_layout()
plt.show()