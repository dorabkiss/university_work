import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from loadData import preProcess
from wordcloud import WordCloud

# Load and preprocess data 
hun_df = preProcess('./data/athlete_events.csv')
# get values from Sport column - this contains many duplicates
sport = hun_df['Sport'].values
# create a set of sports containing unique elements only
list_of_sports = list(set(sport))
print('Total number of sport where Hungarian athletes competed: ', hun_df['Sport'].nunique())

# get values from Event column
events = hun_df['Event'].values
# create a set with unique elements only   
list_of_events = list(set(events))
print('number of events: ',len(list_of_events))

# create wordcloud
wordcloud = WordCloud(collocations=False, 
width=800, 
height=400, 
background_color='white',
stopwords=['Water', 'Ice', 'Modern']).generate(" ".join(sport))
# Generate plot
plt.figure( figsize=(16,8) )
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
