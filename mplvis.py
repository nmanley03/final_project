import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football1.csv")
avgage = data['age'].mean()
print(avgage)
#Some players ages appearing as 0, as well as birthday field. Clean data and replace 0 in age with avg age of 23
data.loc[data['birthday'] == 0, 'age'] = 23

# Create filters by league
pl = data.loc[data['league'] == 'Premier League']
champ = data.loc[data['league'] == 'Championship']
l1 = data.loc[data['league'] == 'EFL League One']
l2 = data.loc[data['league'] == 'EFL League Two']

#Creating a list of top 4 teams in Premier League to filter pl df
topfour_list = ['Liverpool', 'Chelsea', 'Manchester United', 'Manchester City']
boolean = pl['Current Club'].isin(topfour_list)
topfour_df = pl[boolean]
print(topfour_df)

#filter topfour_df to just forwards
forward_df = topfour_df.loc[topfour_df['position'] == 'Forward']

# merge Premier league and Championship; merge League 1 and League 2
toplgs = pd.concat([pl, champ], axis=0)
bottomlgs = pd.concat([l1, l2], axis=0)

#Filter bottom2 to only contain Irish players
irish = bottomlgs.loc[bottomlgs['nationality'] == 'Republic of Ireland']
irish.sort_values('goals_overall')

x = irish["minutes_played_overall"].head(10)
y = irish["goals_overall"].head(10)
z = irish["full_name"].head(10)

plt.scatter(x,y, marker="x", color="red")
plt.title('Number of goals scored by Irish Players vs Minutes Played - EFL L1 & L2')
plt.xlabel('Overall minutes played')
plt.ylabel('Goals Scored')
plt.show()


# Minutes Players minutes played overall in PL vs age
plt.scatter('age', 'minutes_played_overall', data=pl, marker="*", color="green", alpha=0.8)
plt.title('Minutes played by Premier League Players vs Age')
plt.xlabel('Age')
plt.ylabel('Minutes played')
plt.show()

#Seaborn visualisations

#Print charts showing the minutes played by each player in each of the top 4 teams
def graphsize():
    sns.set(rc={"figure.figsize":(5, 5)})


graphsize()
sns.relplot(x='minutes_played_overall', y='age', hue='position', col='Current Club', data=topfour_df)
plt.xlabel('minutes played')
plt.ylabel('age')
plt.show()

#Chart showing counting nationalities in the top 4 teams

plt.figure(figsize=(15,10))

g = sns.countplot('nationality', data=topfour_df, palette="Set1", order=topfour_df['nationality'].value_counts().sort_values(ascending=False).index)
g.set_xticklabels(g.get_xticklabels(),rotation=45)
g.set_title("Counting the number of players of each Nationality in Top 4 Premier League teams", fontsize=15)
g.set_xlabel("", fontsize=12)
g.set_ylabel("Count", fontsize=12)
plt.show()

#Chart showing
avggoal = forward_df.groupby(['Current Club'])['goals_overall'].mean().round(0)
print(avggoal)

#Show goals scored by position for top 4 clubs
sns.catplot(x='Current Club', kind = 'count', palette='viridis', data=topfour_df, hue='position')
plt.xlabel('team')
plt.ylabel('goals scored')
plt.show()