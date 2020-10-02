from .Util import MRV, LCV, toRemove, verify, makeConsistent

def removeArcs(obj, arcs, cur):
    for neighbour in obj.graph[cur]:
        arcs.remove((neighbour, cur))

def putArcs(obj, arcs, cur):
    for neighbour in obj.graph[cur]:
        arcs.add((neighbour, cur))

def BackTrack(obj, Mrv, arcs):
    if Mrv.finished():
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    Mrv.remove(current)
    Values = LCV(obj, cur)
    obj.givenValue[cur] = True
    removeArcs(obj, arcs, cur)
    makeConsistent(obj, set(arcs))
    for value in Values:
        Removed = toRemove(obj, cur, value[1])
        for rem in Removed:
            Mrv.decrease((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].discard(rem[1])
        BackTrack(obj, Mrv, arcs)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    Mrv.add(current)
    obj.givenValue[cur] = False
    putArcs(obj, arcs, cur)

def ArcConsistent_MRV_LCV(obj):
    arcs = set()
    for i in range(1,obj.variables + 1):
        for j in obj.graph[i]:
            arcs.add((i,j))
    Mrv = MRV(obj)
    BackTrack(obj, Mrv, arcs)
    if not verify(obj):
        raise Exception("Computed Answer does not satisfy all the constraints")