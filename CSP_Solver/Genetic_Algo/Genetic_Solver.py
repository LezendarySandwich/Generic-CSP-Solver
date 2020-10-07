from . import Genetic_Util as gu

def Genetic_Solver(obj, populationSize, generations = gu.big):
    population = gu.generateInitailPopulation(obj, populationSize)
    while obj.stop == 0 and generations > 0:
        population = gu.nextGeneration(obj, population, k = populationSize // 2)
        generations -= 1
    if obj.stop == 1:
        for fitness, values in population:
            if fitness == 0:
                print(values[1:obj.variables + 1])
                break
    else:
        print("Answer could not be found")