import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.api.types import CategoricalDtype
from loadData import preProcess, filterMedalsOnly

# load data
hun_df = preProcess('./data/athlete_events.csv')

plt.figure(figsize=(9, 6))
ax = sns.scatterplot(x="Height", 
y="Weight", 
data=hun_df,
hue='Sex', 
edgecolor='none',
s=20, 
alpha=0.5,
palette={"Male": "#18a1cd", "Female":"#fa8c00"})

plt.title('Height and weight of Hungarian athletes', size=16, pad=20, weight='heavy')
ax.set_xlabel('Height (cm)', size=14, labelpad=10)
ax.set_ylabel('Weight (kg)', size=14, labelpad=10)
plt.tight_layout()
plt.show()