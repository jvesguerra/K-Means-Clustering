import csv
import random
import math

data = []
options = []
selected = []   # the user input
max_selection = 2
index_arr = []
xy_arr = []
k_centroids = []
rand_k = []
dist_list1 = []
dist_list2 = []

# Part 1. GET DATA
# open csv file then save data in rows to data array
# with open("./data/wine.csv",'r') as file:
#     csvfile = csv.reader(file)
#     for row in csvfile:
#         data.append(row)

with open("./sample.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

options = data[0];
data_length = len(data)

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
        index_arr.append(choice)    # saves the index of the attributes

n_cluster = int(input("Enter n cluster: "))
selected.append(n_cluster)
#print(selected)

# Part 2.

# create the collection of x and y data points
for i in range(0,data_length):
    xy = [data[i][index_arr[0]],data[i][index_arr[1]]]
    xy_arr.append(xy)

# get k data points
while len(k_centroids) != max_selection:
    random_k = random.randint(1,(data_length-1))
    rand_k.append(random_k)
    k_centroids.append(xy_arr[random_k])

kc_length = len(k_centroids)
xy_length = len(xy_arr)

# get the distances
for kc in range(0,kc_length):    # loop k centroids
    for xy in range(1,xy_length):          # loop data points
        eudistance = 0
        for index in range(0,2):
            x = float(xy_arr[xy][index])
            c = float(k_centroids[kc][index])
            eudistance = ((x - c)**2) + eudistance
        eudistance = math.sqrt(eudistance)
        xy_arr[xy].append(eudistance)


# print(xy_arr[rand_k[0]])
# print(xy_arr[rand_k[1]])

# index 2 is distance from first k centroid
# index 3 is distance from second k centroid

# print xy table with distances
for xy in range(1,xy_length):
    print(xy_arr[xy])

# get which datapoint is close
for kc in range(0,kc_length):
    for xy in range(1,xy_length):
        ind = 2 + kc
        #if xy_arr[xy][int] < xy_arr[rand_k[0]][ind]:
        #print(xy_arr[xy][ind])
            