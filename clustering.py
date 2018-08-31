import random
from random import seed, randrange
import math
from csv import reader


# Load a CSV File
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row: continue
            dataset.append(row)
    return dataset


def str_column_to_flt(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


def getDist(dataset):
    distances = list()
    for i1 in range(0, len(dataset)):
        dist = list()
        for i2 in range(0, len(dataset)):
            x = 0
            for i3 in range(0, len(dataset[0])):
                x += (dataset[i2][i3] - dataset[i1][i3]) * (dataset[i2][i3] - dataset[i1][i3])

            dist.append(x)
        distances.append(dist)

    return distances


def singleLinkClustering(distances):

    initialList = list()

    for i4 in range(0, len(distances)):
        newList = list()
        newList.append(i4)
        initialList.append(newList)


    while(len(initialList)>1):

        data = [0] * len(initialList)

        for i6 in range(0, len(initialList)):
            data[i6] = [0] * len(initialList)

        min2 = 10000
        for i1 in range(0, len(initialList)):
            for i2 in range(i1+1, len(initialList)):
                min1 = 10000
                for i3 in range(0, len(initialList[i1])):
                    for i4 in range(0, len(initialList[i2])):
                        x = distances[initialList[i1][i3]][initialList[i2][i4]]

                        if min1>x:
                            min1 = x
                data[i1][i2] = min1
                data[i2][i1] = min1

        min = 100000
        ptn1 = -1
        ptn2 = -1
        for i5 in range(0, len(initialList)):
            for i6 in range(0, len(initialList)):
                if min>data[i5][i6] and i5 is not i6:
                    min = data[i5][i6]
                    ptn1 = i5
                    ptn2 = i6

        print(initialList[ptn1], " and ", initialList[ptn2], " form the cluster at distance ", min)
        initialList.append(initialList[ptn1]+initialList[ptn2])

        del initialList[ptn1]
        del initialList[ptn2-1]


def completeLinkClustering(distances):

    initialList = list()

    for i4 in range(0, len(distances)):
        newList = list()
        newList.append(i4)
        initialList.append(newList)

    while (len(initialList) > 1):

        data = [0] * len(initialList)

        for i6 in range(0, len(initialList)):
            data[i6] = [0] * len(initialList)

        min2 = 10000
        for i1 in range(0, len(initialList)):
            for i2 in range(i1 + 1, len(initialList)):
                max = -1
                for i3 in range(0, len(initialList[i1])):
                    for i4 in range(0, len(initialList[i2])):
                        x = distances[initialList[i1][i3]][initialList[i2][i4]]

                        if max < x:
                            max = x
                data[i1][i2] = max
                data[i2][i1] = max

        min = 100000
        ptn1 = -1
        ptn2 = -1
        for i5 in range(0, len(initialList)):
            for i6 in range(0, len(initialList)):
                if min > data[i5][i6] and i5 is not i6:
                    min = data[i5][i6]
                    ptn1 = i5
                    ptn2 = i6

        print(initialList[ptn1], " and ", initialList[ptn2], " form the cluster at distance ", min)
        initialList.append(initialList[ptn1] + initialList[ptn2])

        del initialList[ptn1]
        del initialList[ptn2 - 1]



dataset = load_csv('Clustering.csv')

for i in range(0, len(dataset[0])):
    str_column_to_flt(dataset, i)


distances = getDist(dataset)
#print(distances)

print("\n")
print("********************Single Link Clustering******************")
singleLinkClustering(distances)
print("\n\n")
print("********************Complete Link Clustering******************")
completeLinkClustering(distances)





















