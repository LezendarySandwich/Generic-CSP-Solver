from sortedcontainers import SortedList

big = 100000000

class MRV:
    def __init__(self, obj):
        self.Ordering = SortedList()
        for i in range(1,obj.variables + 1):
            self.Ordering.add((len(obj.domains[i]),i))
    def finished(self):
        return len(self.Ordering) == 0
    def minimum(self):
        return self.Ordering[0]
    def remove(self, element):
        self.Ordering.discard(element)
    def add(self, element):
        self.Ordering.add(element)
    def decrease(self, rem):
        # rem = [length, variable]
        self.remove(rem)
        self.add((rem[0]-1,rem[1]))
    def increase(self, rem):
        self.remove(rem)
        self.add((rem[0]+1,rem[1]))

def LCV(obj, cur):
    Values = []
    for value in obj.domains[cur]:
        curr = 0
        obj.value[cur] = value
        for neighbour in obj.graph[cur]:
            if obj.givenValue[neighbour] == True:
                continue
            for Nval in obj.domains[neighbour]:
                obj.value[neighbour] = Nval
                for constraint in obj.graphConstraints[cur][neighbour]:
                    if not eval(constraint):
                        curr += 1
                        break
        Values.append((curr, value))
    Values.sort()
    return Values

def toRemove(obj, cur, value):
    Removed = []
    obj.value[cur] = value
    for neighbour in obj.graph[cur]:
        if obj.givenValue[neighbour]:
            continue
        for Nval in obj.domains[neighbour]:
            obj.value[neighbour] = Nval
            for constraint in obj.graphConstraints[cur][neighbour]:
                if not eval(constraint):
                    Removed.append((neighbour, Nval))
                    break
    return Removed

def verify(obj, getFault = False):
    for constraint in obj.AllConstraints:
        if not eval(constraint):
            return False
    return True