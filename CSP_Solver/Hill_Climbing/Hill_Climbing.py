""" 
heuristic : Minimize the number of constraints failed
"""
import random
from CSP_Solver import Util as ut
from .Hill_Climbing_Util import FastVerify, writeFaults, deleteFaults, defaultFaults

def findBest(obj, Faults):
    mn = ut.big
    best = []
    for va in range(obj.variables + 1):
        for value in obj.domainHelp[va]:
            if mn > Faults[va][value] - Faults[va][obj.value[va]]:
                mn = Faults[va][value] - Faults[va][obj.value[va]]
                best = [(va, value)]
            elif mn == Faults[va][value] - Faults[va][obj.value[va]]:
                best.append((va,value))
    Best = random.choice(best)
    return Best, mn

def Iter(obj, Faults, known, allowedSideMoves):
    best, mn = findBest(obj, Faults)
    if mn > 0 or (mn == 0 and allowedSideMoves <= 0):
        return False, 0
    (va, val) = best
    deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    writeFaults(obj = obj, Faults = Faults, cur = va,known = known)
    return True, -1 if mn == 0 else 0

def TabuIter(obj, Faults, known, allowedSideMoves, tabu):
    best, mn = findBest(obj, Faults)
    if mn > 0 or (mn == 0 and allowedSideMoves <= 0):
        return False, 0
    (va, val) = best
    previous = obj.value[va]
    obj.value[va] = val
    if mn == 0 and tabu.find(obj):
        obj.value[va] = previous
        return True, 0
    else:
        tabu.push(obj)
    obj.value[va] = previous
    deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    writeFaults(obj = obj, Faults = Faults, cur = va,known = known)
    return True, -1 if mn == 0 else 0

def HillClimbing(obj, known = None, allowedSideMoves = 0, tabuSize = 0, iterations = ut.big):
    obj.createRandomInstance()
    Faults = defaultFaults(obj, known)
    if tabuSize == 0:
        while iterations > 0:
            cont, neg = Iter(obj, Faults, known, allowedSideMoves)
            if not cont:
                break
            allowedSideMoves += neg
            iterations -= 1
    else:
        tabu = ut.Tabu(tabuSize)
        tabu.push(obj)
        while iterations > 0:
            cont, neg = TabuIter(obj, Faults, known, allowedSideMoves, tabu)
            if not cont:
                break
            allowedSideMoves += neg
            iterations -= 1
    if not FastVerify(obj, Faults):
        print("Answer does not satisfy all constraints")
        return False
    else :
        print(obj.value[1:obj.variables + 1])
        return True