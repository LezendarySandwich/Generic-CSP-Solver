import copy, random
from CSP_Solver.Util import big

def generateInitailPopulation(obj, populationSize):
    population = []
    for i in range(populationSize):
        obj.createRandomInstance()
        population.append((fitnessValue(obj, obj.value), copy.deepcopy(obj.value)))
    return population

def randomMutation(obj, values, mutationProbability = 0.04):
    return [random.choice(obj.domainHelp[i]) if i is not 0 and random.uniform(0,1) <= mutationProbability else values[i] for i in range(len(values))]

def fitnessValue(obj, values):
    fitness = 0
    for va in range(1,len(values)):
        for neighbour in obj.graph[va]:
            satisfies = True
            for constraint in obj.graphConstraints[va][neighbour]:
                if not eval(constraint, {"value": values}):
                    satisfies = False
                    break
            if not satisfies:
                fitness += 1
    if fitness == 0:
        obj.stop = 1
    return fitness

def tournamentFindParent(obj, currentPopulation, k, indexes):
    k = min(k, len(currentPopulation))
    chooseFrom = random.sample(indexes, k)
    # Now we need to find the fittest among them
    best, mn = [], big
    for i in chooseFrom:
        if mn > currentPopulation[i][0]:
            mn = currentPopulation[i][0]
            best = [currentPopulation[i][1]]
        elif mn == currentPopulation[i][0]:
            best.append(currentPopulation[i][1])
    return random.choice(best)

def tournamentSelection(obj, currentPopulation, k):
    indexes = [i for i in range(0, len(currentPopulation))]
    parent1 = tournamentFindParent(obj, currentPopulation, k, indexes)
    parent2 = tournamentFindParent(obj, currentPopulation, k, indexes)
    return parent1, parent2

def nextGeneration(obj, currentPopulation, k = None, crossoverProbability = .74):
    if k is None:
        k = len(currentPopulation) // 2
    newPopulation = []
    while len(newPopulation) < len(currentPopulation):
        parent1, parent2 = tournamentSelection(obj, currentPopulation, k)
        if random.uniform(0,1) <= crossoverProbability:
            newPopulation.extend(singlePointCrossover(obj, parent1, parent2))
        else:
            child1, child2 = randomMutation(obj, parent1), randomMutation(obj, parent2)
            newPopulation.extend(((fitnessValue(obj, child1), child1), (fitnessValue(obj, child2), child2)))
    return newPopulation

def singlePointCrossover(obj, parent1, parent2):
    crossOverPoint = random.randint(1,len(parent1) - 1)
    offspring1 = parent1[: crossOverPoint + 1] + parent2[crossOverPoint + 1 :]
    offspring2 = parent2[: crossOverPoint + 1] + parent1[crossOverPoint + 1 :]
    offspring1 = randomMutation(obj, offspring1)
    offspring2 = randomMutation(obj, offspring2)
    return (fitnessValue(obj, offspring1), offspring1), (fitnessValue(obj, offspring2), offspring2)