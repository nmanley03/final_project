# import packages
import pandas as pd

# import csv
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football.csv")

print(data)

# Create filters by league
pl = data.loc[data['league'] == 'Premier League']
champ = data.loc[data['league'] == 'Championship']
l1 = data.loc[data['league'] == 'League 1']
l2 = data.loc[data['league'] == 'League 2']

# merge Premier league and Championship; merge League 1 and League 2
top2 = pd.concat([pl, champ], axis=0)
bottom2 = pd.concat([l1, l2], axis=0)
print(top2)
print(bottom2)

# Calculate total minutes played for each distinct nationality playing in Premier League in 2020/21
nationalitydata = pl.groupby(['nationality'])['minutes_played_overall'].sum().round(0)
pd.set_option('display.max_rows', None)
print('Total minutes played per each nationality in the top tier of English professional football in 2020/21 season')
print(nationalitydata)

# Print the top scoring players from Republic of Ireland in League 1 and League 2

# Filter bottom2 to only contain Irish players
irish = bottom2.loc[bottom2['nationality'] == 'Republic of Ireland']
print(irish)
irishscorers = irish.groupby(['full_name'])['goals_overall'].sum()
pd.set_option('display.max_rows', None)
print('Top scoring irish players in League 1 & League 2 in the 2020/21 season')
print(irishscorers)
