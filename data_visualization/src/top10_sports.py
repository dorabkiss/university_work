import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from loadData import preProcess

# Load and preprocess data 
df = preProcess('./data/athlete_events.csv')
# for all sports hun_df['Sport'].value_counts().plot(kind='bar',ax=ax, color='#18a1cd')
# groupby sport, then select top 10 (by number of athletes competing in tht sport)
top10_popular_sports = df.groupby(['Sport']).size().nlargest(10)

fig, ax = plt.subplots(figsize=(9,6))
top10_popular_sports.plot(kind='bar',ax=ax, color='#18a1cd', rot=20)

plt.title('Number of athletes by sport', size=16, pad=20, weight='heavy')
ax.set_xlabel('Sport', size=14, labelpad=10) 
ax.set_ylabel('Number of athletes', size=14, labelpad=10)

plt.tight_layout()
plt.show()