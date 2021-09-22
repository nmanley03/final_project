from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#import data file
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football1.csv")
print(data)
avgage = data['age'].mean()
print(avgage)
#Some players ages appearing as 0, as well as birthday field. Clean data and replace with avg age of 23.1
data.loc[data['birthday'] == 0, 'age'] = 23
print(data)

# Create filters by league
pl = data.loc[data['league'] == 'Premier League']
#champ = data.loc[data['league'] == 'Championship']
#l1 = data.loc[data['league'] == 'EFL League One']
#l2 = data.loc[data['league'] == 'EFL League Two']

team = data['Current Club']

#Seaborn bar chart 'Comparing squad sizes in the Premier League' sorted
def graphsize():
    sns.set(rc={"figure.figsize":(10, 5)})


graphsize()
sns.countplot(y=team,  data=pl, order=pl['Current Club'].value_counts().index)
plt.title("Comparing Squad Sizes in the Premier League")
plt.xlabel('No. of Players')
plt.ylabel('Team')
plt.show()

arsenal = pl.loc[pl['Current Club'] == 'Arsenal']

#Creating a list of top 4 teams in Premier League to filter pl df
topfour_list = ['Liverpool', 'Chelsea', 'Manchester United', 'Manchester City']
boolean = pl['Current Club'].isin(topfour_list)
topfour_df = pl[boolean]
print(topfour_df)

#Print charts showing the minutes played by each player in each of the top 4 teams
def graphsize():
    sns.set(rc={"figure.figsize":(5, 5)})


graphsize()
sns.relplot(x='minutes_played_overall', y='age', hue='position', col='Current Club', data=topfour_df)
plt.xlabel('minutes played')
plt.ylabel('age')
plt.show()

#G5 Seaborn catplot 'league' by wavecsv
#sns.catplot(x='position', col='Position', data=bigsix_df, col_wrap=4, order=arsenal['position'].value_counts().index, kind="count")
#plt.show()