import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterColumn, filterMedalsOnly

# load data
hun_df = preProcess('./data/athlete_events.csv')
medal_reversed = CategoricalDtype(categories=reversed(hun_df.Medal.cat.categories), ordered=True)
hun_df['Medal'] = hun_df['Medal'].astype(medal_reversed)

# filter dataframe to contain rows with medals only, then select Summer Games only
filtered_df = filterMedalsOnly(hun_df)
filtered_df = filterColumn(filtered_df, 'Season', 'Summer')

# count medals in team events as one
hun_df_no_duplicates = filtered_df.drop_duplicates(['Games', 'Event', 'Medal']).reset_index(drop=True)

# cross tabulate Sex and Medal columns so that we get medal count by gender
df2 = pd.crosstab(hun_df_no_duplicates['Sex'], hun_df_no_duplicates['Medal'])

cols = ['#D4AF37', '#BCC6CC', '#cd7f32']
ax = df2.plot.barh(stacked=True, figsize=(8,4), color=cols)
handles, labels = ax.get_legend_handles_labels()

ax.legend(handles, labels, bbox_to_anchor=(1.0, 1.0), frameon=False)
plt.title('Medals won by Hungary according to gender', size=16, pad=20, weight='heavy')
ax.set_xlabel('Number of medals won', size=14, labelpad=10)
ax.set_ylabel('Gender', size=14, labelpad=10) 
ax.set_yticklabels(['Men', 'Women'])

# Annotate bars with values
for p in ax.patches:
    ax.annotate(str(p.get_width()), xy=(p.get_x() + p.get_width()/2, p.get_y()+ p.get_height()/2 ), ha='center', va='center')

plt.tight_layout()
plt.show()