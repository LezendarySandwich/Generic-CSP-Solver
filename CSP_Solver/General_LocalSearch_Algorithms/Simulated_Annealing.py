"""
Cooling :: Linear w.r.t iterations
"""
from .Util import Instance, big
from math import exp
from random import uniform
from time import time

def simulated_annealing(obj, iterations = big, temperature = 10000, decreaseConstant = 1, timeout = 10):
    start = time()
    global_dictionary = dict()
    obj.createRandomInstance()
    state = Instance(obj, global_dictionary)
    while iterations > 0 and temperature > 0:
        if time() - start > timeout:
            return
        if state.currentFitness == 0:
            break
        va, val, delta = state.randNeighbour(obj)
        if delta > 0:
            state.changeVal(obj, va, val, global_dictionary)
        elif exp(delta / temperature) >= uniform(0,1):
            state.changeVal(obj, va, val, global_dictionary)
        iterations -= 1
        temperature -= decreaseConstant
    if state.currentFitness == 0:
        obj.stop = 1
        
