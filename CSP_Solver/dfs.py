from .verifySolution import verify

def BackTracking(obj, cur):
    if cur > obj.variables:
        if verify(obj):
            obj.stop = 1
            print(obj.value[1:obj.variables+1])
        return
    for value in obj.domains[cur]:
        obj.givenValue[cur] = False
        obj.value[cur] = value
        BackTracking(obj, cur + 1)
        if obj.stop:
            return 
        obj.givenValue[cur] = True

def dfs(obj):
    BackTracking(obj, 1)