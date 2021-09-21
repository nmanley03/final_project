#import packages
import pandas as pd

#import csv
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football.csv")

print(data)

#Calculate total minutes played for each distinct nationality playing in top 4 English leagues in 2020/21
nationalitydata = data.groupby(['nationality'])['minutes_played_overall'].sum().round(0)
pd.set_option('display.max_rows', None)
print('Total minutes played per each nationality in the top 4 tiers of English professional football in 2020/21 season')
print(nationalitydata)