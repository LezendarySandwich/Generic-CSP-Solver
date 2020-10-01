""" 
heuristic : Minimize the number of constraints failed
"""
import random
from . import Util as ut
from .Hill_Climbing import FastVerify

def writeFaults(obj, Faults, cur, known, add = 1):
    if (cur, obj.value[cur]) in known:
        for (va, value) in known[(cur, obj.value[cur])]:
            Faults[va][value] += add
    else :
        Vl = []
        for va in obj.graph[cur]:
            previousVal = obj.value[va]
            for value in obj.domains[va]:
                obj.value[va] = value
                for constraint in obj.graphConstraints[cur][va]:
                    if not eval(constraint,{"value":obj.value}):
                        Faults[va][value] += add
                        Vl.append((va, value))
                        break
            obj.value[va] = previousVal
        known[(cur, obj.value[cur])] = Vl

def deleteFaults(obj, Faults, cur, known):
    writeFaults(obj, Faults, cur, known, -1)

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

def defaultFaults(obj, known):
    Faults = [dict() for i in range(obj.variables + 1)]
    for i in range(1,obj.variables + 1):
        for value in obj.domainHelp[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i, known)
    return Faults

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