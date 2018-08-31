import random
import math

population = 50
crossover_prob = 0.5
features = 2
f = random.uniform(0,2)


def initialization():
    members = [0] * population
    for i in range(0, population):
        members[i] = list()
        for i1 in range(0, features):
            x = random.uniform(0,1)
            members[i].append(x)
    return members


#For maximization problem
def fitness_func(x):
    return math.sin(x[0])+math.cos(x[1])


def mutation(members):
    mutants = [0] * population
    for i in range(0, population):
        random_vectors = list()
        mutants[i] = list()
        j=0
        while j<3:
            x = random.uniform(0,1)
            y = int(population*x)
            if y not in random_vectors:
                random_vectors.append(y)
                j = j+1

        rn0 = members[random_vectors[0]]
        rn1 = members[random_vectors[1]]
        rn2 = members[random_vectors[2]]

        diff_vector = list()
        for k in range(0, features):
            diff_vector.append(f*(rn1[k]-rn2[k]))

        for k in range(0, features):
            mutants[i].append(diff_vector[k]+rn0[k])

    return mutants


def crossover(members, mutants):

    children = [0] * population
    for i in range(0, population):
        children[i] = list()

        for j in range(0, features):
            x = random.uniform(0,1)

            if x<=crossover_prob:
                children[i].append(members[i][j])
            else:
                children[i].append(mutants[i][j])

    return children


def finalTournament(members):

    count = 0
    maxFitness = list()
    while True:

        generation = list()
        mutants = mutation(members)
        children = crossover(members, mutants)
        maxi = -1
        for i in range(0, population):
            x = fitness_func(members[i])
            y = fitness_func(children[i])

            if x > y:
                generation.append(members[i])
                if x > maxi:
                    maxi = x
            else:
                generation.append(children[i])
                if y > maxi:
                    maxi = y

        maxFitness.append(maxi)
        count = count + 1

        if count>=5:
            cnt = 0
            for k in range(1, 6):
                if maxFitness[len(maxFitness)-k] == maxFitness[len(maxFitness)-k-1]:
                    cnt = cnt+1
                    continue
                else:
                    break

            if cnt == 5 or count == 50:
                break


    return generation


members = initialization()
generation = finalTournament(members)
print(generation)