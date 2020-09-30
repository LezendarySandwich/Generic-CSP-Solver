""" 
heuristic : Number of constraints satisfied
"""
import copy
from . import Util as ut

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
                    if not eval(constraint):
                        Faults[va][value] += add
                        Vl.append((va, value))
                        break
            obj.value[va] = previousVal
        known[(cur, obj.value[cur])] = Vl

def deleteFaults(obj, Faults, cur, known):
    writeFaults(obj, Faults, cur, known, -1)

def findBest(obj, Faults):
    mn = ut.big
    best = (None, None)
    for va in range(obj.variables + 1):
        for value in obj.domainHelp[va]:
            if mn > Faults[va][value] - Faults[va][obj.value[va]]:
                mn = Faults[va][value] - Faults[va][obj.value[va]]
                best = (va, value)
    return best, mn

def Iter(obj, Faults, known):
    best, mn = findBest(obj, Faults)
    if mn >= 0:
        return False
    (va, val) = best
    deleteFaults(obj, Faults, va, known)
    obj.value[va] = val
    writeFaults(obj, Faults, va, known)
    return True

def defaultFaults(obj, known):
    Faults = [dict() for i in range(obj.variables + 1)]
    for i in range(1,obj.variables + 1):
        for value in obj.domainHelp[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i, known)
    return Faults

def HillClimbing_with_memoisation(obj, known = dict()):
    obj.createRandomInstance()
    Faults = defaultFaults(obj, known)
    tot = 0
    while Iter(obj, Faults, known):
        pass
    if not ut.verify(obj):
        print("Answer does not satisfy all constraints")
        return False
    else :
        print(obj.value[1:obj.variables + 1])
        return True