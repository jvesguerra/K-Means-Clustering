import csv
import random
import math
import copy

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
k = 2
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

print(xy_arr)
# xy_arr is the original datapoints
# datapoints would be use for the loop

# LOOP HERE

# get k data points
datapoints = copy.deepcopy(xy_arr)
while len(k_centroids) != k:
    random_k = random.randint(1,(data_length-1))
    rand_k.append(random_k)
    k_centroids.append(xy_arr[random_k])

kc_length = len(k_centroids)
xy_length = len(datapoints)

# FOR TESTING
k_centroids.clear()
rand_k.clear()
rand_k = [4,6]
k_centroids = [[2,2],[4,4]]
# CHANGE LATER

# get the distances
for kc in range(0,kc_length):    # loop k centroids
    for xy in range(1,xy_length):          # loop data points
        eudistance = 0
        for index in range(0,2):
            x = float(datapoints[xy][index])
            c = float(k_centroids[kc][index])
            eudistance = ((x - c)**2) + eudistance
        eudistance = math.sqrt(eudistance)
        datapoints[xy].append(eudistance)

# get which datapoint is close then group by k
for xy in range(1,xy_length):
    for kc in range(0,kc_length):
        if kc == 0:
            min = datapoints[xy][kc]
            group = xy_arr[rand_k[kc]]
        else:
            if datapoints[xy][kc] < min:
                min = datapoints[xy][kc]
                group = xy_arr[rand_k[kc]]
    datapoints[xy].append(group)

# group = 2 + k
group_ind = 2 + kc_length # index of the groupings

for xy in range(1,xy_length):
    print(datapoints[xy])   

# PART 3. Solve for new centroid

# count class
class_count = {}
for i in range(0,k):
    for j in range(1,xy_length):
        if j not in rand_k:
            if datapoints[j][group_ind] == xy_arr[rand_k[i]]:
                if class_count.get(i) is None:
                    class_count[i] = 1
                else:
                    class_count[i] += 1

print(class_count)


# reset values
rand_k.clear()
k_centroids.clear()
datapoints.clear()

