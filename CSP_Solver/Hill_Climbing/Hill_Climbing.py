""" 
heuristic : Minimize the number of constraints failed
"""
import random
from CSP_Solver import Util as ut

def writeFaults(obj, Faults, cur, add = 1):
    for va in obj.graph[cur]:
        previousVal = obj.value[va]
        for value in obj.domains[va]:
            obj.value[va] = value
            for constraint in obj.graphConstraints[cur][va]:
                if not eval(constraint,{"value":obj.value}):
                    Faults[va][value] += add
                    break
        obj.value[va] = previousVal

def deleteFaults(obj, Faults, cur):
    writeFaults(obj, Faults, cur, -1)

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

def Iter(obj, Faults, allowedSideMoves):
    best, mn = findBest(obj, Faults)
    if mn > 0 or (mn == 0 and allowedSideMoves <= 0):
        return False, 0
    (va, val) = best
    deleteFaults(obj, Faults, va)
    obj.value[va] = val
    writeFaults(obj, Faults, va)
    return True, -1 if mn == 0 else 0

def TabuIter(obj, Faults, allowedSideMoves, tabu):
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
    deleteFaults(obj, Faults, va)
    obj.value[va] = val
    writeFaults(obj, Faults, va)
    return True, -1 if mn == 0 else 0

def defaultFaults(obj):
    Faults = [dict() for i in range(obj.variables + 1)]
    for i in range(1,obj.variables + 1):
        for value in obj.domainHelp[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i)
    return Faults

def FastVerify(obj, Faults):
    for i in range(1,obj.variables + 1):
        if Faults[i][obj.value[i]] > 0:
            return False
    return True

def HillClimbing(obj, allowedSideMoves = 0, tabuSize = 0, iterations = ut.big):
    obj.createRandomInstance()
    Faults = defaultFaults(obj)
    if tabuSize == 0:
        while iterations > 0:
            cont, neg = Iter(obj, Faults, allowedSideMoves)
            if not cont:
                break
            allowedSideMoves += neg
            iterations -= 1
    else:
        tabu = ut.Tabu(tabuSize)
        tabu.push(obj)
        while iterations > 0:
            cont, neg = TabuIter(obj, Faults, allowedSideMoves, tabu)
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