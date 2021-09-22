# import packages
import pandas as pd

# import csv
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

#Grouping averages goals scored by team in the premier league, grouped again by each position
avggoal = pl.groupby(['Current Club','position'])['goals_overall'].mean().round(0)
pd.set_option('display.max_rows', None)
print('Average goals scored by each position per team in the PL is as follows:')
print(avggoal)






# merge Premier league and Championship; merge League 1 and League 2
top2 = pd.concat([pl, champ], axis=0)
bottom2 = pd.concat([l1, l2], axis=0)
#print(top2)
#print(bottom2)

# Calculate average minutes played for each distinct nationality playing in Premier League in 2020/21
nationalitydata = pl.groupby(['nationality'])['minutes_played_overall'].mean().round(0)
pd.set_option('display.max_rows', None)
print('Average minutes played per each nationality in the top tier of English professional football in 2020/21 season')
print(nationalitydata)

# Print the top scoring players from Republic of Ireland in League 1 and League 2

#Filter bottom2 to only contain Irish players who have scored more than 5 goals
irish = bottom2.loc[bottom2['nationality'] == 'Republic of Ireland']
irishscorers = bottom2.loc[bottom2['goals_overall'] > 5]

#Print list of irish players in L1 & L2 who have scored more than 5 goals in 2020/21 season
scorers = irishscorers[["full_name","goals_overall"]]
print('The Irish Players who have scored more than 5 goals in L1 or L2 this season are:')
print(scorers.sort_values(by='goals_overall', axis=0, ascending=False))

#The irish players in L1 & L2 iterated
for index, row in irishscorers.iterrows():
      print('The player ID ', index, ' refers to the Irish Player: ', row['full_name'])

