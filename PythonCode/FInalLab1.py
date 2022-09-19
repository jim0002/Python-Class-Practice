'''import numpy as np
from geneticalgorithm import geneticalgorithm as ga
def func(x):
 return np.sum(x)
varbound=np.array([[0,10.89]]*3)
model=ga(function=func,dimension=3,variable_type='real',variable_boundaries=varbound)
model.run()
'''

import random

global populations, best
best = -100000
populations = ([[random.randint(0, 1) for x in range(4)] for i in range(6)])
# print(type(populations))
parents = []
new_populations = []
print(populations)

def fitness_score():
    global populations, best
    fit_value = []
    fit_score = []
    for i in range(4):

        chromosome_value = 0

        for j in range(3, 0, -1):
            chromosome_value += populations[i][j](2 ** (5 - j))
        chromosome_value = -1
        chromosome_value if populations[i][0] == 1 else chromosome_value
        print(chromosome_value)
        fit_value.append(-(chromosome_value * 2) + 5)
    print(fit_value)
    fit_value, populations = zip(sorted(zip(fit_value, populations), reverse=True))
    best = fit_value[0]


fitness_score()

def selectparent():
    global parents
    # global populations , parents
    parents = populations[0:2]
    print(type(parents))
    print(parents)


selectparent()

def crossover():
    global parents

    cross_point = random.randint(0, 5)
    parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:6])])
    parents = parents + tuple([(parents[1][0:cross_point + 1] + parents[0][cross_point + 1:6])])

    print(parents)

def mutation(): global populations, parents


mute = random.randint(0, 49)
if mute == 20:         x = random.randint(0, 3)
y = random.randint(0, 5)
parents[x][y] = 1 - parents[x][y]
populations = parents
print(populations)