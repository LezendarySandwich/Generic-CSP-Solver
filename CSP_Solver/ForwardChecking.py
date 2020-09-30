from .Util import toRemove, verify

def BackTracking(obj, cur):
    if cur > obj.variables:
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
        return
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        Removed = toRemove(obj, cur, value)
        Possible = True
        for rem in Removed:
            obj.domains[rem[0]].discard(rem[1])
            if len(obj.domains[rem[0]]) == 0:
                Possible = False
        if Possible:
            BackTracking(obj, cur + 1)
        if obj.stop:
            return 
        for rem in Removed:
            obj.domains[rem[0]].add(rem[1])
    obj.givenValue[cur] = False

def forwardChecking(obj):
    BackTracking(obj, 1)
    if not verify(obj):
        raise Exception("Computed Answer does not satisfy all the constraints")