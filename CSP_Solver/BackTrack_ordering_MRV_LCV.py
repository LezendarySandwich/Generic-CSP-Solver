from sortedcontainers import SortedList
from .verifySolution import verify

def BackTrack(obj, Ordering):
    if len(Ordering) == 0:
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    current = Ordering[0]
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    Ordering.discard(Ordering[0])
    Values = []
    for value in obj.domains[cur]:
        curr = 0
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
            if obj.givenValue[neighbour[0]] == True:
                continue
            for Nval in obj.domains[neighbour[0]]:
                obj.value[neighbour[0]] = Nval
                if not eval(neighbour[1]):
                    Removed.append((neighbour[0], Nval))
        for rem in Removed:
            Ordering.remove((len(obj.domains[rem[0]]), rem[0]))
            obj.domains[rem[0]].discard(rem[1])
            Ordering.add((len(obj.domains[rem[0]]), rem[0]))
        BackTrack(obj, Ordering)
        if obj.stop:
            return 
        for rem in Removed:
            Ordering.remove((len(obj.domains[rem[0]]), rem[0]))
            obj.domains[rem[0]].add(rem[1])
            Ordering.add((len(obj.domains[rem[0]]), rem[0]))
    Ordering.add(current)
    obj.givenValue[cur] = False


def orderedBackTrack_MRV_LCV(obj):
    Ordering = SortedList()
    for i in range(1,obj.variables + 1):
        Ordering.add((len(obj.domains[i]),i))
    BackTrack(obj, Ordering)
    if not verify(obj):
        raise Exception("Computed Answer does not satisfy all the constraints")