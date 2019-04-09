import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from loadData import preProcess, filterColumn

# Load and preprocess data 
df = preProcess('./data/athlete_events.csv')

# select summer games only
df = filterColumn(df, 'Season', 'Summer')
# select a subset of data and drop duplicate ID from the same year
df = df[['Year', 'ID', 'Age', 'Sex']].drop_duplicates(['Year', 'ID']).reset_index(drop=True)

# drop ID column
df.drop('ID', axis=1, inplace=True)
df2 = df.copy()
df.set_index(['Year','Sex'], inplace=True, append=True)
#group by year and sex columns, and calculate average age for each group
df_grouped = df.groupby(level=['Year', 'Sex'])['Age'].mean()
# Move 'Sex' level out of row index to columns index
avg_age_vs_time = df_grouped.unstack()

fig, ax = plt.subplots(figsize=(8, 6))

avg_age_vs_time.plot(ax = ax, linewidth=3)
sns.scatterplot(x="Year", 
y="Age", 
data=df2,
hue="Sex",
s=14,
alpha=0.4,
edgecolor='none',
palette={"Male": "#18a1cd", "Female":"#fa8c00"})
# add legend, x and y labels, x ticks and title
ax.legend(labels=['Men', 'Women'],bbox_to_anchor=(1.0, 1.0))

ax.set_xlabel('Year', size=14, labelpad=10)
ax.set_ylabel('Average age (years)', size=14, labelpad=10)
ax.set_title("Average age of Hungarian athletes in the Olympics", pad=20, weight='heavy')

years = list(range(1896, 2022, 8))
plt.xticks(years)

plt.tight_layout()
plt.show()