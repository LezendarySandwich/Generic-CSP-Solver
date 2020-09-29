from .verifySolution import verify

def BackTracking(obj, cur):
    if cur > obj.variables:
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        obj.value[cur] = value
        Removed = []
        for neighbour in obj.graph[cur]:
            if obj.givenValue[neighbour[0]]:
                continue 
            for Nval in obj.domains[neighbour[0]]:
                obj.value[neighbour[0]] = Nval
                if not eval(neighbour[1]):
                    Removed.append((neighbour[0], Nval))
        for rem in Removed:
            obj.domains[rem[0]].discard(rem[1])
        BackTracking(obj, cur + 1)
        if obj.stop:
            return 
        for rem in Removed:
            obj.domains[rem[0]].add(rem[1])
    obj.givenValue[cur] = False

def BackTrack(obj):
    BackTracking(obj, 1)
    if not verify(obj):
        raise Exception("Computed Answer does not satisfy all the constraints")