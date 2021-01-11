"""
Works for bivariate as well as multivariate constraints
"""

from time import time

def BackTracking(obj, cur, start, timeout):
    if time() - start > timeout:
        return 
    if cur > obj.variables:
        obj.stop = 1
        return
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        obj.value[cur] = value
        canBeValue = True
        if not obj.multivariate:
            for neighbour in obj.graph[cur]:
                if not obj.givenValue[neighbour]:
                    continue
                for constraint in obj.graphConstraints[cur][neighbour]:
                    if not eval(constraint, {"value": obj.value}):
                        canBeValue = False
                        break
                if not canBeValue:
                    break
        else:
            for constraint, neighbours in obj.multivariateGraph[cur]:
                check = True
                for neighbour in neighbours:
                    if not obj.givenValue[neighbour]:
                        check = False
                        break
                if check and not eval(constraint, {"value": obj.value}):
                    canBeValue = False
                    break
        if not canBeValue:
            continue
        BackTracking(obj, cur + 1, start, timeout)
        if obj.stop:
            return 
    obj.givenValue[cur] = False

def BackTrack(obj, timeout = 10):
    start = time()
    BackTracking(obj, 1, start, timeout)