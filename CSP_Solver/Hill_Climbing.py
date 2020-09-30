""" 
heuristic : Number of constraints satisfied
"""
from . import Util as ut

def failedConstraints(obj, cur):
    failed = 0
    for neighbour in obj.graph[cur]:
        if not eval(neighbour[1]):
            failed += 1
    return failed

def findBest(obj, failedCount):
    mn = ut.big
    best = (None, None)
    for va in range(1,obj.variables + 1):
        previous = obj.value[va]
        for value in obj.domainHelp[va]:
            if value == previous:
                continue
            obj.value[va] = value
            failedVa = failedConstraints(obj, va)
            if mn > failedVa - failedCount[va]:
                mn = failedVa - failedCount[va]
                best = (va, value)
            if mn < 0:
                return best , mn
        obj.value[va] = previous
    return best, mn

def changeState(obj, best):
    (va, value) = best
    for neighbour in obj.graph[va]:
        

def HillClimbing(obj):
    obj.createRandomInstance()
    failedCount = [failedConstraints(obj,i) for i in range(obj.variables + 1)]
    # totalFailure = 0
    # for i in range(1,obj.variables + 1):
    #     totalFailure += failedCount[i]
    tot = 0 
    while True:
        tot += 1
        best, mn = findBest(obj, failedCount)
        if mn >= 0:
            break
        (va, value) = best
        failedCount[va] += mn
        obj.value[va] = value
    if not ut.verify(obj):
        print("Answer does not satisfy all constraints")
    else :
        print(obj.value[1:obj.variables + 1], failedCount[1:obj.variables+1])
    print(tot)