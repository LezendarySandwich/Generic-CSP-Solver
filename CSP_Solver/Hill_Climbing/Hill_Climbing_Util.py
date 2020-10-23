import enum
from queue import Queue
from CSP_Solver.Util import big

class choice(enum.Enum):
    chooseBest = 1
    chooseRandom = 2
    greedyBias = 3

class Tabu:
    def __init__(self, queueSize):
        self.fifo = Queue(maxsize=queueSize)
        self.search = dict()
    def removeFirst(self):
        rem = self.fifo.get()
        self.search[rem] -= 1
        if self.search[rem] == 0:
            self.search.pop(rem)
    def push(self, obj):
        if self.fifo.full():
            self.removeFirst()
        self.fifo.put(tuple(obj.value))
        if tuple(obj.value) in self.search:
            self.search[tuple(obj.value)] += 1
        else :
            self.search[tuple(obj.value)] = 1
    def find(self, obj):
        return tuple(obj.value) in self.search

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
        for value in obj.domains[i]:
            Faults[i][value] = 0
    for i in range(1,obj.variables + 1):
        writeFaults(obj, Faults, i, known)
    return Faults

def FastVerify(obj, Faults):
    for i in range(1,obj.variables + 1):
        if Faults[i][obj.value[i]] > 0:
            return False
    return True
