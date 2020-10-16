from CSP_Solver.Util import toRemove, MRV
from copy import deepcopy
from .Hill_Climbing.Hill_Climbing_with_restarts import Hill_Climbing_with_restarts, choice

def BackTrack(obj, Mrv):
    if Mrv.finished():
        obj.stop = 1
        print(obj.value[1:])
        return
    if Mrv.size() < obj.variables // 2:
        flag = Hill_Climbing_with_restarts(obj = obj, memoization=True,allowedSideMoves=30,choice=choice.greedyBias,application=100)
        if flag:
            obj.stop = 1
            return
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
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
        BackTrack(obj, Mrv)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    Mrv.add(current)
    obj.givenValue[cur] = False

def My_Algo(obj):
    Mrv = MRV(obj)
    BackTrack(obj, Mrv)
    if not obj.stop:
        print("No valid Solution Exists")