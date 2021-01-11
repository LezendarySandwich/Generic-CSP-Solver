"""
Works for bivariate as well as multivariate constraints
"""

from CSP_Solver.Util import toRemove
from time import time

def BackTracking(obj, cur, start, timeout):
    if time() - start > timeout:
        return
    if cur > obj.variables:
        obj.stop = 1
        return
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        Possible = True
        Removed = toRemove(obj, cur, value)
        for rem in Removed:
            obj.domains[rem[0]].discard(rem[1])
            if len(obj.domains[rem[0]]) == 0:
                Possible = False
        if Possible:
            BackTracking(obj, cur + 1, start, timeout)
        if obj.stop:
            return 
        for rem in Removed:
            obj.domains[rem[0]].add(rem[1])
    obj.givenValue[cur] = False

def ForwardChecking(obj, timeout = 10):
    start = time()
    BackTracking(obj, 1, start, timeout)