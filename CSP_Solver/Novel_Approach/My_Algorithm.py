from CSP_Solver.Util import toRemove, MRV
from copy import deepcopy
from CSP_Solver.Hill_Climbing.Hill_Climbing_with_restarts import Hill_Climbing_with_restarts, choice
from time import time

def BackTrack(obj, Mrv, split, allowedSideMoves, tabuSize, tries, start, timeout):
    if Mrv.finished():
        obj.stop = 1
        return
    if time() - start > timeout:
        return
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    if Mrv.size() < split:
        flag = Hill_Climbing_with_restarts(obj = obj, memoization=True,allowedSideMoves=allowedSideMoves,tabuSize=tabuSize,choice=choice.greedyBias,application=tries)
        if flag:
            obj.stop = 1
            return
    Mrv.remove(current)
    obj.givenValue[cur] = True
    iterableList = deepcopy(obj.domains[cur])
    for value in iterableList:
        Removed = toRemove(obj, cur, value)
        obj.domains[cur] = {value}
        for rem in Removed:
            Mrv.decrease((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].discard(rem[1])
        BackTrack(obj, Mrv, split, allowedSideMoves, tabuSize, tries, start, timeout)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    Mrv.add(current)
    obj.givenValue[cur] = False

def My_Algo(obj, split = None, allowedSideMoves = None, tabuSize = 0, tries = None, timeout = 10):
    if allowedSideMoves == None:
        allowedSideMoves = obj.variables << 1
    split = (obj.variables + 1) // 2 if split is None else split
    start = time()
    Mrv = MRV(obj)
    BackTrack(obj, Mrv, (obj.variables + 1) // 2, allowedSideMoves, tabuSize, tries, start, timeout)