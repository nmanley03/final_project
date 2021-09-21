import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#import data
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football.csv")

# Create filters by league
pl = data.loc[data['league'] == 'Premier League']
champ = data.loc[data['league'] == 'Championship']
l1 = data.loc[data['league'] == 'EFL League One']
l2 = data.loc[data['league'] == 'EFL League Two']

# merge Premier league and Championship; merge League 1 and League 2
top2 = pd.concat([pl, champ], axis=0)
bottom2 = pd.concat([l1, l2], axis=0)
print(top2)
print(bottom2)

#Filter bottom2 to only contain Irish players
irish = bottom2.loc[bottom2['nationality'] == 'Republic of Ireland']

plt.pyplot.scatter(irish)
plt.show()