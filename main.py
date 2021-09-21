#import pandas
import pandas as pd

#import csv file
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football.csv")

# print heads and info on dataframe
print(data.head())
print(data.info())
print(data.shape)

#Count unique nationalities & clubs in the data set, and print.
nationality_count = data['nationality'].nunique()
club_count = data['Current Club'].nunique()
print("This data set contains statistics for players from a total of " + str(club_count)+ " clubs across the Premier League & Championship in the 2020/21 season, from a total of " + str(nationality_count) + " countries.")