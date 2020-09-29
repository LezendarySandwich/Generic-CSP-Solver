def verify(obj, getFault = False):
    for i in range(1,obj.variables + 1):
        for neighbour in obj.graph[i]:
            if not eval(neighbour[1]):
                if getFault:
                    print(neighbour[1])
                return False
    return True