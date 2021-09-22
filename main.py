#import pandas
import pandas as pd

#import csv file
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football1.csv")
avgage = data['age'].mean()
print(avgage)
#Some players ages appearing as 0, as well as birthday field. Clean data and replace with avg age of 23
data.loc[data['birthday'] == 0, 'age'] = 23

# print heads and info on dataframe
print(data.head())
print(data.info())
print(data.shape)

#Count unique nationalities & clubs in the data set, and print.
nationality_count = data['nationality'].nunique()
club_count = data['Current Club'].nunique()
league_count = data['league'].nunique()

print("This data set contains statistics for players from a total of " + str(club_count)+ " clubs across the " +str(league_count)+ " professional English leagues in the 2020/21 season, who hail from a total of " + str(nationality_count) + " countries.")