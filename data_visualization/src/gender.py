import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from loadData import preProcess, filterColumn

# Load and preprocess data 
hun_df = preProcess('./data/athlete_events.csv')

# drop duplicate entries from the same Olympic Game 
hun_df_distinct_ids = hun_df.drop_duplicates(['Year', 'ID']).reset_index(drop=True)

# select Summer Games only
hun_df_distinct_ids = filterColumn(hun_df_distinct_ids, 'Season', 'Summer')

colours = ['#18a1cd', '#fa8c00']

fig, ax = plt.subplots(figsize=(6, 4))
ax.pie(hun_df_distinct_ids['Sex'].value_counts(sort=False),
            colors=colours,
            startangle=60,
            wedgeprops = {'linewidth':0.5, 'edgecolor':'lightgrey', 'width':0.7},
            autopct='  %.0f%%',
            pctdistance=0.6, 
            labeldistance=1.1)

# Equal aspect ratio ensures that pie is drawn as a circle.
ax.axis('equal')
# Put a legend next to the chart, hide frame
plt.legend(hun_df_distinct_ids['Sex'].cat.categories,bbox_to_anchor=(1,0.5),loc="center left", frameon=False)
plt.title('Gender of athletes', size=16, pad=20, weight='heavy')
plt.tight_layout()
 
plt.show()