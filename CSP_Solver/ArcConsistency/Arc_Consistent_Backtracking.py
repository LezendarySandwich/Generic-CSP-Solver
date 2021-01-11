from CSP_Solver.Util import MRV, LCV, toRemove, verify
from .ArcConsistency_Util import makeConsistent, removeArcs, putArcs
from time import time

def BackTrack(obj, Mrv, arcs, start, timeout):
    if Mrv.finished():
        obj.stop = 1
        return
    if time() - start > timeout:
        return 
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    Mrv.remove(current)
    Values = LCV(obj, cur)
    obj.givenValue[cur] = True
    RemovedArcValues = makeConsistent(obj, set(arcs))
    removed = removeArcs(obj, arcs, cur)
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
    putArcs(obj, arcs, removed)

def ArcConsistent_MRV_LCV(obj, timeout = 10):
    start = time()
    arcs = set()
    for i in range(1,obj.variables + 1):
        for j in obj.graph[i]:
            arcs.add((i,j))
    Mrv = MRV(obj)
    BackTrack(obj, Mrv, arcs, start, timeout)