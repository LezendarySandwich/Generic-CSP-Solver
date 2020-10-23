from . import Genetic_Util as gu
from time import clock

def Genetic_Solver(obj, populationSize, generations = gu.big, timeout = 10):
    start = clock()
    population = gu.generateInitailPopulation(obj, populationSize)
    while obj.stop == 0 and generations > 0:
        if clock() - start > timeout:
            return 
        population = gu.nextGeneration(obj, population, k = populationSize // 2)
        generations -= 1
    if obj.stop == 1:
        for fitness, values in population:
            if fitness == 0:
                obj.value = values
                break