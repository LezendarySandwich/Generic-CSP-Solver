""" 
heuristic : Number of constraints satisfied
"""
import copy
from . import Util as ut

def writeFaults(obj, Faults, cur, add = 1):
    for va in obj.graph[cur]:
        previousVal = obj.value[va]
        for value in obj.domains[va]:
            obj.value[va] = value
            for constraint in obj.graphConstraints[cur][va]:
                if not eval(constraint):
                    Faults[va][value] += add
                    break
        obj.value[va] = previousVal

def deleteFaults(obj, Faults, cur):
    writeFaults(obj, Faults, cur, -1)

def findBest(obj, Faults):
    mn = ut.big
    best = (None, None)
    for va in range(obj.variables + 1):
        for value in obj.domainHelp[va]:
            if mn > Faults[va][value] - Faults[va][obj.value[va]]:
                mn = Faults[va][value] - Faults[va][obj.value[va]]
                best = (va, value)
    return best, mn

def Iter(obj, Faults):
    best, mn = findBest(obj, Faults)
    if mn >= 0:
        return False
    (va, val) = best
    deleteFaults(obj, Faults, va)
    obj.value[va] = val
    writeFaults(obj, Faults, va)
    return True

def defaultFaults(obj):
    Faults = [dict() for i in range(obj.variables + 1)]
    for i in range(1,obj.variables + 1):
        for value in obj.domainHelp[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i)
    return Faults

def HillClimbing(obj):
    obj.createRandomInstance()
    Faults = defaultFaults(obj)
    tot = 0
    while Iter(obj, Faults):
        pass
    if not ut.verify(obj):
        print("Answer does not satisfy all constraints")
        return False
    else :
        print(obj.value[1:obj.variables + 1])
        return True