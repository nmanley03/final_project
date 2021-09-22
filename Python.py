import pandas as pd
import numpy as np

#import csv file
data = pd.read_csv(r"/Users/niallmanley/Downloads/Final_Project/202021Football1.csv")

#Function to filter data to Current Club column, and drop duplicates in order to print each different team
teams = data['Current Club']
print(teams)
unique_teams = teams.drop_duplicates()

#Convert list of teams without duplicates into dictionary
allteams = unique_teams.to_dict()
print('Number of teams in the top 4 divisions of English football:')
print(len(allteams))

#Convert unique_teams into numpy array and print the list of teams
ary = unique_teams.to_numpy()
print(ary.shape)
print(type(ary))
print('The teams are as follows:')
print(ary)