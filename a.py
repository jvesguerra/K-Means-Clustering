import csv
import math

data = []
options = []
selected = []   # the user input
max_selection = 2

# open csv file then save data in rows to data array
with open("./data/wine.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

options = data[0];

# PRINT MENU
for j in range(0,max_selection):
    print("MENU")
    for i in range(0, len(options)):
        print("[",i,"] ",options[i])

    choice = int(input("Enter attribute [n]: "))
    selected.append(options[choice])

n_cluster = int(input("Enter n cluster: "))
selected.append(n_cluster)
print(selected)