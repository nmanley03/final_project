import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#import data
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football1.csv")

# Create filters by league
pl = data.loc[data['league'] == 'Premier League']
champ = data.loc[data['league'] == 'Championship']
l1 = data.loc[data['league'] == 'EFL League One']
l2 = data.loc[data['league'] == 'EFL League Two']

# merge Premier league and Championship; merge League 1 and League 2
top2 = pd.concat([pl, champ], axis=0)
bottom2 = pd.concat([l1, l2], axis=0)

#Filter bottom2 to only contain Irish players
irish = bottom2.loc[bottom2['nationality'] == 'Republic of Ireland']
irish.sort_values('goals_overall')

x = irish["minutes_played_overall"].head(10)
y = irish["goals_overall"].head(10)
z = irish["full_name"].head(10)

plt.scatter(x,y, marker="x", color="red")
plt.title('Number of goals scored by Irish Players vs Minutes Played - EFL L1 & L2')
plt.xlabel('Overall minutes played')
plt.ylabel('Goals Scored')
plt.show()

ax = irish.hist(column='goals_overall', by='league', bins=10, grid=False, figsize=(8,10), layout=(3,1), sharex=True, zorder=2, rwidth=0.9)
for i,x in enumerate(ax):
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0, color='#eeeeee', zorder=1)
    x.set_xlabel("Goals Scored by Irish in L1 & L2", labelpad=20, weight='bold', size=12)
    if i == 1:
        x.set_ylabel("Number of players", labelpad=50, weight='bold', size=12)
plt.show()

# Minutes Players minutes played overall in PL vs age
plt.scatter('age','minutes_played_overall', data=pl, marker="x", color="red")
plt.title('Minutes played by Premier League Players vs Age')
plt.xlabel('Age')
plt.ylabel('Minutes played')
plt.show()





plt.scatter('age', 'minutes_played_overall', data=pl, color="#146870", marker='*', markersize=3, alpha=0.1)
plt.xlabel('Age')
plt.ylabel('Minutes Played')
plt.title('Minutes played by Premier League Players vs Age', loc='left')
plt.show()