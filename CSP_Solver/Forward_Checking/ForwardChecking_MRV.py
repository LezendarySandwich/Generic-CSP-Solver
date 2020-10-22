from CSP_Solver.Util import toRemove, MRV
from time import clock

def BackTrack(obj, Mrv, start, timeout):
    if clock() - start > timeout:
        return 
    if Mrv.finished():
        obj.stop = 1
        return
    current = Mrv.minimum()
    cur = current[1]
    if len(obj.domains[cur]) == 0:
        return 
    Mrv.remove(current)
    obj.givenValue[cur] = True
    for value in obj.domains[cur]:
        Removed = toRemove(obj, cur, value)
        for rem in Removed:
            Mrv.decrease((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].discard(rem[1])
        BackTrack(obj, Mrv, start, timeout)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    Mrv.add(current)
    obj.givenValue[cur] = False

def ForwardChecking_MRV(obj, timeout):
    start = clock()
    Mrv = MRV(obj)
    BackTrack(obj, Mrv, start, timeout)