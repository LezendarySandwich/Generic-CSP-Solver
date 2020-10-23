from CSP_Solver.Util import MRV, LCV, toRemove, verify
from .ArcConsistency_Util import makeConsistent, removeArcs, putArcs
from time import clock

def BackTrack(obj, Mrv, arcs, start, timeout):
    if Mrv.finished():
        obj.stop = 1
        return
    if clock() - start > timeout:
        return 
    current = Mrv.minimum()
    cur = current[1]
    # print(cur,len(obj.domains[cur]))
    if len(obj.domains[cur]) == 0:
         return 
    Mrv.remove(current)
    Values = LCV(obj, cur)
    obj.givenValue[cur] = True
    # removeArcs(obj, arcs, cur)
    RemovedArcValues = makeConsistent(obj, set(arcs))
    # print(RemovedArcValues,cur,Mrv.Ordering)
    for va, val in RemovedArcValues:
        Mrv.correct(va, len(obj.domains[va]))
    for value in Values:
        Removed = toRemove(obj, cur, value[1])
        for rem in Removed:
            Mrv.decrease((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].discard(rem[1])
        BackTrack(obj, Mrv, arcs, start, timeout)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    for va, val in RemovedArcValues:
        obj.domains[va].add(val)
    for va, val in RemovedArcValues:
        Mrv.correct(va, len(obj.domains[va]))
    Mrv.add(current)
    obj.givenValue[cur] = False
    # putArcs(obj, arcs, cur)

def ArcConsistent_MRV_LCV(obj, timeout = 10):
    start = clock()
    arcs = set()
    for i in range(1,obj.variables + 1):
        for j in obj.graph[i]:
            arcs.add((i,j))
    Mrv = MRV(obj)
    BackTrack(obj, Mrv, arcs, start, timeout)