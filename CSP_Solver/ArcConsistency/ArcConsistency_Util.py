def removeArcs(obj, arcs, cur):
    for neighbour in obj.graph[cur]:
        arcs.remove((neighbour, cur))

def putArcs(obj, arcs, cur):
    for neighbour in obj.graph[cur]:
        arcs.add((neighbour, cur))

def RemoveInconsistent(obj, arc, Removed):
    remove = []
    x, y = arc
    for valx in obj.domains[x]:
        satisfies = False
        obj.value[x] = valx
        for valy in obj.domains[y]:
            sat = True
            obj.value[y] = valy
            for constraint in obj.graphConstraints[x][y]:
                if not eval(constraint, {"value":obj.value}):
                    sat = False
                    break
            if sat:
                satisfies = True
                break
        if not satisfies:
            remove.append((x, valx))
    for x, valx in remove:
        obj.domains[x].remove(valx)
    Removed += remove
    return len(remove) > 0

def makeConsistent(obj, setOfArcs):
    # Arcs should be as tuple in listOfArcs
    # arc(x,y) : x -> y
    Removed = []
    while len(setOfArcs) > 0:
        arc = setOfArcs.pop()
        if RemoveInconsistent(obj, arc, Removed):
            for neighbour in obj.graph[arc[0]]:
                # if not obj.givenValue[neighbour]: 
                    setOfArcs.add((neighbour, arc[0]))
    return Removed