"""
Works for bivariate as well as multivariate constraints
"""

from CSP_Solver.Util import verify
from time import time

def BackTracking(obj, cur, start, timeout):
    if time() - start > timeout:
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
    start = time()
    BackTracking(obj, 1, start, timeout)