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


def removeClass(dataset):
    for row in dataset:
        del row[-1]

    return dataset


def str_column_to_flt(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


def updateCenter(classes):

    newList = list()

    for j1 in range(0, len(classes)):
        part = classes[j1]
        center = list()
        if part:
            for j2 in range(0, len(part[0])):
                sum = 0
                for j3 in range(0, len(part)):
                    sum = sum + part[j3][j2]
                sum = sum/len(part)
                center.append(sum)
            newList.append(center)

    return newList


def cluster(dataset, clist):

    classes = [0] * len(clist)

    while(True):

        for k3 in range(0, len(clist)):
            classes[k3] = list()

        for i1 in range(0, len(dataset)):
            part = dataset[i1]

            max = 10000
            index = -1

            for i3 in range(0, len(clist)):
                dist = 0
                for i5 in range(0, len(clist[0])):
                    dist += (part[i5]-clist[i3][i5])*(part[i5]-clist[i3][i5])

                if max>dist:
                    max = dist
                    index = i3

            classes[index].append(part)

        newClist = updateCenter(classes)

        if sorted(newClist) == sorted(clist):
            return classes
        else:
            clist = newClist


k = 3

dataset = load_csv('iris_dataset.csv')

dataset = removeClass(dataset)

for i in range(0, len(dataset[0])):
    str_column_to_flt(dataset, i)


rows = len(dataset)
cols = len(dataset[0])

c = list()
num = list()
it = 0
while it<k:
    n = random.uniform(0,1)
    x = int(n*rows)
    if x not in num:
        center = list()
        for i4 in range(0, len(dataset[0])):
            center.append(dataset[x][i4])
        c.append(center)
        num.append(x)
        it = it+1

clusters = cluster(dataset, c)

for k1 in range(0, len(clusters)):
    print("length ",len(clusters[k1]))
    for k2 in range(0, len(clusters[k1])):
        print(clusters[k1][k2])
