import enum

class choice(enum.Enum):
    chooseBest = 1
    chooseRandom = 2
    greedyBias = 3


def writeFaults(obj, Faults, cur, known = None, add = 1):
    if known is not None:
        if (cur, obj.value[cur]) in known:
            for (va, value) in known[(cur, obj.value[cur])]:
                Faults[va][value] += add
        else:
            Vl = []
            for va in obj.graph[cur]:
                previousVal = obj.value[va]
                for value in obj.domains[va]:
                    obj.value[va] = value
                    for constraint in obj.graphConstraints[cur][va]:
                        if not eval(constraint,{"value":obj.value}):
                            Faults[va][value] += add
                            Vl.append((va, value))
                            break
                obj.value[va] = previousVal
            known[(cur, obj.value[cur])] = Vl
    else :
        for va in obj.graph[cur]:
            previousVal = obj.value[va]
            for value in obj.domains[va]:
                obj.value[va] = value
                for constraint in obj.graphConstraints[cur][va]:
                    if not eval(constraint,{"value":obj.value}):
                        Faults[va][value] += add
                        break
            obj.value[va] = previousVal

def deleteFaults(obj, Faults, cur, known):
    writeFaults(obj, Faults, cur, known, -1)

def defaultFaults(obj, known):
    Faults = [dict() for i in range(obj.variables + 1)]
    for i in range(1,obj.variables + 1):
        for value in obj.domainHelp[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i, known)
    return Faults

def FastVerify(obj, Faults):
    for i in range(1,obj.variables + 1):
        if Faults[i][obj.value[i]] > 0:
            return False
    return True