from .verifySolution import verify
from .MRV_manager import MRV

def BackTrack(obj, Mrv):
    if Mrv.finished():
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    Mrv.remove(current)
    Values = []
    for value in obj.domains[cur]:
        curr = 0
        obj.value[cur] = value
        for neighbour in obj.graph[cur]:
            if obj.givenValue[neighbour[0]] == True:
                continue
            for Nval in obj.domains[neighbour[0]]:
                obj.value[neighbour[0]] = Nval
                if not eval(neighbour[1]):
                    curr += 1
        Values.append((curr, value))
    Values.sort()
    obj.givenValue[cur] = True
    for value in Values:
        Removed = []
        obj.value[cur] = value[1]
        for neighbour in obj.graph[cur]:
            if obj.givenValue[neighbour[0]]:
                continue
            for Nval in obj.domains[neighbour[0]]:
                obj.value[neighbour[0]] = Nval
                if not eval(neighbour[1]):
                    Removed.append((neighbour[0], Nval))
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

def orderedBackTrack_MRV_LCV(obj):
    Mrv = MRV(obj)
    BackTrack(obj, Mrv)
    if not verify(obj):
        raise Exception("Computed Answer does not satisfy all the constraints")