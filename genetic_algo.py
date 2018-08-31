import random

population = 50
crossover_prob = 0.8
mutation_prob = 0.2
n = 10


def fitness_func(x):
    num1 = int("".join(str(a) for a in x), 2)
    return num1


def initialization(n):
    members = [0] * 50
    for i in range(0, 50):
        members[i] = list()
        for i1 in range(0, n):
            x = random.uniform(0,1)
            if x-0.5>0:
                members[i].append(1)
            else:
                members[i].append(0)
    return members


def selection(members):

    a1 = random.uniform(0,1)
    a2 = random.uniform(0,1)
    if a1 == a2:
        while a1 == a2:
            a2 = random.uniform(0,1)

    x = int(population*a1)
    y = int(population*a2)

    max = -1
    if fitness_func(members[x])>fitness_func(members[y]):
        max = fitness_func(members[x])
    else:
        max = fitness_func(members[y])

    return [int(x) for x in list('{0:010b}'.format(max))]


def crossover(newPop):

    cross_pop = list()
    for i3 in range(0, len(newPop)-1):
        x = random.uniform(0,1)
        y = int(n*x)
        child1 = list()
        child2 = list()

        for i4 in range(0, y):
            child1.append(newPop[i3][i4])
            child2.append(newPop[i3+1][i4])

        for i7 in range(y, n):
            child1.append(newPop[i3+1][i7])
            child2.append(newPop[i3][i7])

        cross_pop.append(newPop[i3])
        cross_pop.append(newPop[i3+1])
        cross_pop.append(child1)
        cross_pop.append(child2)

    return cross_pop


def mutation(cross_pop):
    m = len(cross_pop)
    y = mutation_prob*m

    mutated = list()
    i4 = 0
    while i4<y:
        a = random.uniform(0, 1)
        x = int(a*m)
        if x not in mutated:
            mutated.append(x)
            bit = random.uniform(0,1)
            flip_bit = int(bit*n)
            if cross_pop[x][flip_bit] == 0:
                cross_pop[x][flip_bit] = 1
            else:
                cross_pop[x][flip_bit] = 0

            i4 = i4+1

    return cross_pop


def main_method(members):

    iterations = int(crossover_prob*population)
    newPopulation = list()

    for i2 in range(0, iterations):
        newPopulation.append(selection(members))

    cross_pop = crossover(newPopulation)
    for row in members:
        if row not in newPopulation:
            cross_pop.append(row)

    cross_pop = mutation(cross_pop)

    newGeneration = list()
    myList = list()

    for i2 in range(0, len(cross_pop)):
        myList.append(fitness_func(cross_pop[i2]))

    sortBy = sorted(range(len(myList)), key=myList.__getitem__)

    for i5 in range(0, 50):
        newGeneration.append(cross_pop[sortBy[i5]])

    return newGeneration


members = initialization(n)

newGeneration = main_method(members)
print(newGeneration)