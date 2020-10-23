""" 
heuristic : Minimize the number of constraints failed
"""
import random
from . import Hill_Climbing_Util as ut

def findBest(obj, Faults, va):
    mn = ut.big
    best = []
    for value in obj.domainHelp[va]:
        if mn > Faults[va][value] - Faults[va][obj.value[va]]:
            mn = Faults[va][value] - Faults[va][obj.value[va]]
            best = [value]
        elif mn == Faults[va][value] - Faults[va][obj.value[va]]:
            best.append(value)
    Best = random.choice(best)
    return Best, mn

def Iter(obj, Faults, known, allowedSideMoves):
    choose_from = []
    for i in range(1,obj.variables + 1):
        if Faults[i][obj.value[i]] > 0:
            choose_from.append(i)
    if len(choose_from) == 0:
        return False, 0
    va = random.choice(choose_from)
    val, mn = findBest(obj, Faults, va)
    if mn > 0 or (mn == 0 and allowedSideMoves <= 0):
        return False, 0
    ut.deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    ut.writeFaults(obj, Faults, va, known)
    return True, -1 if mn == 0 else 0

def TabuIter(obj, Faults, known, allowedSideMoves, tabu):
    choose_from = []
    for i in range(1,obj.variables + 1):
        if Faults[i][obj.value[i]] > 0:
            choose_from.append(i)
    if len(choose_from) == 0:
        return False, 0
    va = random.choice(choose_from)
    val, mn = findBest(obj, Faults, va)
    if mn > 0 or (mn == 0 and allowedSideMoves <= 0):
        return False, 0
    previous = obj.value[va]
    obj.value[va] = val
    if mn == 0 and tabu.find(obj):
        return True, 0
    else:
        tabu.push(obj)
    obj.value[va] = previous
    ut.deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    ut.writeFaults(obj, Faults, va, known)
    return True, -1 if mn == 0 else 0

def HillClimbing_chooseRandom(obj, known = None, allowedSideMoves = 0, tabuSize = 0, iterations = ut.big, memoization = False):
    if memoization and known is None:
        known = dict()
    obj.createRandomInstance()
    Faults = ut.defaultFaults(obj, known)
    if tabuSize == 0:
        while iterations > 0:
            cont, neg = Iter(obj, Faults, known, allowedSideMoves)
            if not cont:
                break
            allowedSideMoves += neg
            iterations -= 1
    else :
        tabu = ut.Tabu(tabuSize)
        tabu.push(obj)
        while iterations > 0:
            cont, neg = TabuIter(obj, Faults, known, allowedSideMoves, tabu)
            if not cont:
                break
            allowedSideMoves += neg
            iterations -= 1
    if not ut.FastVerify(obj, Faults):
        return False
    else:
        return True