
def BackTrack(obj, cur):
    if obj.stop:
        return 
    if cur > obj.variables:
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    for value in obj.domains[cur]:
        obj.value[cur] = value
        Removed = []
        for neighbour in obj.graph[cur]:
            for Nval in obj.domains[neighbour[0]]:
                obj.value[neighbour[0]] = Nval
                if not eval(neighbour[1]):
                    Removed.append((neighbour[0], Nval))
        for rem in Removed:
            obj.domains[rem[0]].discard(rem[1])
        BackTrack(obj, cur + 1)
        for rem in Removed:
            obj.domains[rem[0]].add(rem[1])