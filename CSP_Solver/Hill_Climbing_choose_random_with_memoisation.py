""" 
heuristic : Minimize the number of constraints failed
"""
import random
from . import Util as ut
from .Hill_Climbing import FastVerify
from .Hill_Climbing_with_memoisation import writeFaults, deleteFaults, defaultFaults

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
    deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    writeFaults(obj, Faults, va, known)
    return True, -1 if mn == 0 else 0

def HillClimbing_choose_random_with_memoisation(obj, known = dict(), allowedSideMoves = 0):
    obj.createRandomInstance()
    Faults = defaultFaults(obj, known)
    while True:
        cont, neg = Iter(obj, Faults, known, allowedSideMoves)
        if not cont:
            break
        allowedSideMoves += neg
    if not FastVerify(obj, Faults):
        print("Answer does not satisfy all constraints")
        return False
    else :
        print(obj.value[1:obj.variables + 1])
        return True