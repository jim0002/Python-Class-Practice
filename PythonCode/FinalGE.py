import numpy as np
import random

population = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Integer Numbers : ", population)
numbers = [0, 1, 2, 3, 4, 5]
fitnesses = []
ratios = []

for i in range(15):
    population[i] = format(population[i], "b")
    str(population[i])
    if (len(population[i]) == 1):
        population[i] = '000' + population[i]
    if (len(population[i]) == 2):
        population[i] = '00' + population[i]

    if (len(population[i]) == 3):
        population[i] = '0' + population[i]


def fitness(x):
    return 15 * x - x ** 2


def ratio(fitness, sum):
    return (fitness / sum) * 100


print("Binary String : ", population)

N = 6  # population size
selectedPopulation = np.random.choice(population, N, replace=False)
print("Selected Population :", selectedPopulation)
print(type(selectedPopulation[0]))

for step in range(5):
    fitnesses = []
    ratios = []
    print(selectedPopulation)
    # CROSSOVER
    crossOvers = []
    crossOvers.append((selectedPopulation[0])[0:2] + (selectedPopulation[2])[2:4])
    crossOvers.append(selectedPopulation[2][0:2] + selectedPopulation[0][2:4])
    crossOvers.append(selectedPopulation[1][0:2] + selectedPopulation[3][2:4])
    crossOvers.append(selectedPopulation[3][0:2] + selectedPopulation[1][2:4])
    crossOvers.append(selectedPopulation[4][0:2] + selectedPopulation[5][2:4])
    crossOvers.append(selectedPopulation[5][0:2] + selectedPopulation[4][2:4])
    print("Crossovers : ", crossOvers)

    selectedPopulation = crossOvers

    # MUTATION
    selectedPopulation[3] = selectedPopulation[3][0:2] + '0' + selectedPopulation[3][3:4]
    selectedPopulation[0] = selectedPopulation[0][0:2] + '1' + selectedPopulation[0][3:4]
    selectedPopulation[4] = selectedPopulation[0][0:2] + '0' + selectedPopulation[4][3:4]
    print("Mutated Populations : ", selectedPopulation[3], selectedPopulation[0], selectedPopulation[4])

    temp = selectedPopulation.copy()

    for i in range(6):
        temp[i] = int(temp[i], 2)

    print("Int Values : ", temp)
    sum = 0
    for i in range(6):
        sum = fitness(temp[i]) + sum

    print("Total Fitness :", sum)
    for i in range(6):
        fitnesses.append(fitness(temp[i]))
        ratios.append(ratio(fitness(temp[i]), sum))

    print("Number       Fitness            Ratio")
    print("-----------------------------------------------------")
    for i in range(6):
        print(" ", temp[i], "          ", fitnesses[i], "            ", ratios[i])