# inspiration for visualising the difference between variables from lecture slides
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loadData import preProcess, filterColumn

# Load and preprocess data 
df = preProcess('./data/athlete_events.csv')

# select summer games only
df = filterColumn(df, 'Season', 'Summer')
# select a subset of data and drop duplicate Id from the same year
df = df[['Year', 'ID', 'Age', 'Sex']].drop_duplicates(['Year', 'ID']).reset_index(drop=True)

# drop ID column
df.drop('ID', axis=1, inplace=True)

df.set_index(['Year','Sex'], inplace=True, append=True)
#group by year and sex columns, and calculate average age for each group
df_grouped = df.groupby(level=['Year', 'Sex'])['Age'].mean()
# Move 'Sex' level out of row index to columns index
avg_age_vs_time = df_grouped.unstack()

# calculate difference between average age values for men and women
difference = avg_age_vs_time['Male'] - avg_age_vs_time['Female']

# find the maximum difference value
max_difference = difference.max()
max_year = difference.idxmax()

male_max = avg_age_vs_time.loc[max_year, 'Male'] 
female_max = avg_age_vs_time.loc[max_year, 'Female']


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=False)

avg_age_vs_time.plot(ax = ax1)

# add legend, x and y labels, x ticks and title
ax1.legend(labels=['Men', 'Women'],bbox_to_anchor=(1.0, 1.0))

ax1.set_xlabel('Year', size=14, labelpad=10)
ax1.set_ylabel('Average age', size=14, labelpad=10)
ax1.set_title("Average age of Hungarian athletes in the Olympics", pad=20, weight='heavy')
# Add text label: shift one year to the left. 
ax1.text(x=max_year-10, y=26, s='largest\ndifference\n in {}'.format(max_year), fontsize=8, horizontalalignment='right')
# Add arrow between inner and outer max.
ax1.annotate('', xy=(max_year, male_max),xytext=(max_year, female_max),arrowprops=dict(arrowstyle='<|-|>',
connectionstyle='arc3,rad=0.0',edgecolor='black',facecolor='black'))

# plot the difference
difference.plot(ax=ax2)
ax2.set_xlabel('Year', size=14, labelpad=10)
ax2.set_ylabel('Difference (years)', size=14, labelpad=10)
ax2.set_title('Difference between the average age of \n male and female athletes', pad=10, weight='heavy') 

# Set the ticks for all axes
years = list(range(1900, 2022, 10))
plt.setp((ax1, ax2), xticks=years)

fig.subplots_adjust(hspace=0.6)
plt.tight_layout()
plt.show()