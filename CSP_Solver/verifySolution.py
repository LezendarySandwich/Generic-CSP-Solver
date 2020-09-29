
def verify(obj):
    for i in range(1,obj.variables + 1):
        for neighbour in obj.graph[i]:
            if not eval(neighbour[1]):
                return 0
    return 1