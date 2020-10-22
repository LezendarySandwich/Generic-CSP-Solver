from CSP_Solver.Util import verify
from time import clock

def BackTracking(obj, cur, start, timeout):
    if clock() - start > timeout:
        return
    if cur > obj.variables:
        if verify(obj):
            obj.stop = 1
        return
    for value in obj.domainHelp[cur]:
        obj.givenValue[cur] = False
        obj.value[cur] = value
        BackTracking(obj, cur + 1, start, timeout)
        if obj.stop:
            return 
        obj.givenValue[cur] = True

def dfs(obj, timeout = 10):
    start = clock()
    BackTracking(obj, 1, start, timeout)