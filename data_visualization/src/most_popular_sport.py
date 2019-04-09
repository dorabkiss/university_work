import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from loadData import preProcess

# Load and preprocess data 
hun_df = preProcess('./data/athlete_events.csv')

fig, ax = plt.subplots(figsize=(9,6))
hun_df['Sport'].value_counts().plot(kind='bar',ax=ax, color='#18a1cd')

# add title, x and y labels 
plt.title('Popularity of sports by number of participants', size=16, pad=20, weight='heavy')
ax.set_xlabel('Sport', size=14, labelpad=10)
ax.set_ylabel('Number of athletes', size=14, labelpad=10)

plt.tight_layout()
plt.show()