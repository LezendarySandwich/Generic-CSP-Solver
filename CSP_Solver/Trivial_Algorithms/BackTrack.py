def BackTracking(obj, cur):
    if cur > obj.variables:
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        obj.value[cur] = value
        canBeValue = True
        for neighbour in obj.graph[cur]:
            if not obj.givenValue[neighbour]:
                continue
            for constraint in obj.graphConstraints[cur][neighbour]:
                if not eval(constraint, {"value": obj.value}):
                    canBeValue = False
                    break
            if not canBeValue:
                break
        if not canBeValue:
            continue
        BackTracking(obj, cur + 1)
        if obj.stop:
            return 
    obj.givenValue[cur] = False

def BackTrack(obj):
    BackTracking(obj, 1)
    if not obj.stop:
        print("No valid Solution Exists")