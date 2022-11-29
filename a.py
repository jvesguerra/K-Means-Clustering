import csv
import random
import math
import copy
import matplotlib.pyplot as plt

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
#open csv file then save data in rows to data array

with open("./data/wine.csv",'r') as file:
    csvfile = csv.reader(file)
    for row in csvfile:
        data.append(row)

output = open('output.txt', 'w')

# with open("./sample.csv",'r') as file:
#     csvfile = csv.reader(file)
#     for row in csvfile:
#         data.append(row)

options = data[0]
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

n_cluster = 11
while n_cluster > 10:
    n_cluster = int(input("Enter n cluster (max is 10): "))
    selected.append(n_cluster)
    k = n_cluster

# Part 2.
# create the collection of x and y data points
for i in range(0,data_length):
    xy = [data[i][index_arr[0]],data[i][index_arr[1]]]
    xy_arr.append(xy)

# xy_arr is the original datapoints
# datapoints would be use for the loop

# get random k centroids
while len(k_centroids) != n_cluster:
    random_k = random.randint(1,(data_length-1))
    if xy_arr[random_k] not in k_centroids:
        k_centroids.append((xy_arr[random_k]))

#k_centroids = [[11.76,2.68],[13.77,1.9]]
#k_centroids = [[2,2],[4,4]]
kc_length = len(k_centroids)

run = 1
while run == 1:
    # get k data points
    datapoints = copy.deepcopy(xy_arr)

    xy_length = len(datapoints)
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
    temp = []
    for xy in range(1,xy_length):
        temp.clear()
        for kc in range(0,kc_length):
            temp.append(datapoints[xy][2+kc])
            min_value = min(temp)
            min_index = temp.index(min_value)
        datapoints[xy].append(k_centroids[min_index])

    # group = 2 + k
    group_ind = 2 + kc_length # index of the groupings

    # PART 3. Solve for new centroid
    # count class

    class_count = {}
    for i in range(0,n_cluster):
        for j in range(1,xy_length):
            if datapoints[j][group_ind] == k_centroids[i]:
                if class_count.get(i) is None:
                    class_count[i] = 1
                else:
                    class_count[i] += 1

    prev_centroids = copy.deepcopy(k_centroids)
    new_centroids = []

    for kc in range(0,kc_length):
        xSum = 0
        ySum = 0
        for xy in range(1,xy_length):
            if datapoints[xy][len(datapoints[1])-1] == k_centroids[kc]:
                xSum += float(datapoints[xy][0]) 
                ySum += float(datapoints[xy][1])
        x = xSum/class_count.get(kc)
        y = ySum/class_count.get(kc)
        new_centroid = [x,y]
        new_centroids.append(new_centroid)

    #print("New",new_centroids)
    if(new_centroids == prev_centroids):
        x_list = [[],[],[],[],[],[],[],[],[],[]]
        y_list = [[],[],[],[],[],[],[],[],[],[]]
        for n in range(0,kc_length):
            print(prev_centroids[n])
            x_list[n].append(prev_centroids[n][0])
            y_list[n].append(prev_centroids[n][1])
            output.write("Centroid ")
            output.write(str(n))
            output.write(" (")
            output.write(str(prev_centroids[n][0]))
            output.write(" ")
            output.write(str(prev_centroids[n][1]))
            output.write(") \n")
            for j in range(1,xy_length):
                if datapoints[j][group_ind] == k_centroids[n]:
                    print(xy_arr[j])
                    x_list[n].append(xy_arr[j][0])
                    y_list[n].append(xy_arr[j][1])
                    output.write(xy_arr[j][0])
                    output.write(" ")
                    output.write(xy_arr[j][1])
                    output.write("\n")

        if k >= 1:
            plt.scatter(x_list[0], y_list[0], c ="blue")
        if k >= 2:
            plt.scatter(x_list[1], y_list[1], c ="orange")
        if k >= 3:
            plt.scatter(x_list[2], y_list[2], c ="green")
        if k >= 4:
            plt.scatter(x_list[3], y_list[3], c ="red")
        if k >= 5:
            plt.scatter(x_list[4], y_list[4], c ="purple")
        if k >= 6:
            plt.scatter(x_list[5], y_list[5], c ="brown")
        if k >= 7:
            plt.scatter(x_list[6], y_list[6], c ="pink")
        if k >= 8:
            plt.scatter(x_list[7], y_list[7], c ="gray")
        if k >= 9:
            plt.scatter(x_list[8], y_list[8], c ="olive")
        if k >= 10:
            plt.scatter(x_list[9], y_list[9], c ="cyan")

        plt.title("Kmeans Scatter Plot")
        plt.show()

        run = 0

    k_centroids.clear()
    k_centroids = copy.deepcopy(new_centroids)
    # reset values
    datapoints.clear()

output.close()
