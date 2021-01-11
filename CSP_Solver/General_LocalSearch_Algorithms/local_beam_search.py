from copy import deepcopy
from .Util import Instance
from numpy.random import choice
from time import time

def initialBeam(obj, k, global_dictionary):
    beam = []
    for i in range(k):
        obj.createRandomInstance()
        beam.append(Instance(obj, global_dictionary))
        if beam[-1].currentFitness == 0:
            obj.stop = 1
    return beam

def debugBeam(beam):
    P = [i.value[1:len(i.value)] for i in beam]
    print(P)

def local_beam_search(obj, k, timeout = 10):
    start = time()
    global_dictionary = dict()
    beam = initialBeam(obj, k, global_dictionary)
    maxFailure = 0
    for i in range(1, obj.variables + 1):
        maxFailure += len(obj.graph[i])
    while len(beam) > 0:
        if time() - start > timeout:
            return
        neighbours = []
        for i in range (len(beam)):
            neighbours.extend(beam[i].bestNeighbours(obj, i))
        probability_distribution = []
        total = 0
        for (fitness, index, va, value) in neighbours:
            if fitness == 0:
                obj.value = deepcopy(beam[index].value)
                obj.value[va] = value
                obj.stop = 1
                break
            probability_distribution.append(maxFailure - fitness)
            total += maxFailure - fitness
        probability_distribution = [probability_distribution[i] / total for i in range(len(probability_distribution))]
        if obj.stop == 1:
            break
        indexes = [i for i in range(len(neighbours))]
        chosenInd = choice(indexes, min(k, len(probability_distribution)), probability_distribution)
        chosen = [neighbours[i] for i in chosenInd]
        NextBeam = []
        for fitness, index, va, value in chosen:
            N = deepcopy(beam[index])
            N.changeVal(obj, va, value, global_dictionary)
            NextBeam.append(N)
        beam = NextBeam

