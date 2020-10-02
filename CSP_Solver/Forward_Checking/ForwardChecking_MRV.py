from CSP_Solver.Util import toRemove, MRV

def BackTrack(obj, Mrv):
    if Mrv.finished():
        obj.stop = 1
        print(obj.value[1:obj.variables+1])
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
        BackTrack(obj, Mrv)
        if obj.stop:
            return 
        for rem in Removed:
            Mrv.increase((len(obj.domains[rem[0]]),rem[0]))
            obj.domains[rem[0]].add(rem[1])
    Mrv.add(current)
    obj.givenValue[cur] = False

def ForwardChecking_MRV(obj):
    Mrv = MRV(obj)
    BackTrack(obj, Mrv)
    if not obj.stop:
        print("No valid Solution Exists")