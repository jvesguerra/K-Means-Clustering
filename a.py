import csv
import math

data = []
options = []
selected = []   # the user input
max_selection = 2

# Part 1. GET DATA
# open csv file then save data in rows to data array
with open("./data/wine.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

options = data[0];

# PRINT MENU
while len(selected) != max_selection:
    print("MENU \n")
    for i in range(0, len(options)):
        print("[",i,"] ",options[i])

    choice = int(input("Enter attribute [n]: "))

    # selected option must be unique
    if options[choice] in selected:
        print("Cannot add selected attribute\n")
    else:
        print("Successfully added",options[choice],"\n")
        selected.append(options[choice])

n_cluster = int(input("Enter n cluster: "))
selected.append(n_cluster)
print(selected)

# Part 2.