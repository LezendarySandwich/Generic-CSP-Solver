from sortedcontainers import SortedList
big = 100000000

class MRV:
    def __init__(self, obj):
        self.Ordering = SortedList()
        self.Help = dict()
        for i in range(1,obj.variables + 1):
            self.Ordering.add((len(obj.domains[i]),i))
            self.Help[i] = len(obj.domains[i])
    def finished(self):
        return len(self.Ordering) == 0
    def size(self):
        return len(self.Ordering)
    def minimum(self):
        return self.Ordering[0]
    def remove(self, element):
        self.Ordering.discard(element)
    def add(self, element):
        if element not in self.Ordering:
            self.Ordering.add(element)
    def decrease(self, rem):
        # rem = [length, variable]
        self.remove(rem)
        self.Help[rem[1]] -= 1
        self.add((rem[0]-1,rem[1]))
    def increase(self, rem):
        self.remove(rem)
        self.Help[rem[1]] += 1
        self.add((rem[0]+1,rem[1]))
    def correct(self, rem, newLen):
        self.remove((self.Help[rem], rem))
        self.Help[rem] = newLen
        self.add((self.Help[rem], rem))

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
                    if not eval(constraint,{"value":obj.value}):
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
                if not eval(constraint,{"value":obj.value}):
                    Removed.append((neighbour, Nval))
                    break
    return Removed

def RemoveInconsistent(obj, arc, Removed):
    remove = []
    x, y = arc
    for valx in obj.domains[x]:
        satisfies = False
        obj.value[x] = valx
        for valy in obj.domains[y]:
            sat = True
            obj.value[y] = valy
            for constraint in obj.graphConstraints[x][y]:
                if not eval(constraint, {"value":obj.value}):
                    sat = False
                    break
            if sat:
                satisfies = True
                break
        if not satisfies:
            remove.append((x, valx))
    for x, valx in remove:
        obj.domains[x].remove(valx)
    Removed += remove
    return len(remove) > 0

def makeConsistent(obj, setOfArcs):
    # Arcs should be as tuple in listOfArcs
    # arc(x,y) : x -> y
    Removed = []
    while len(setOfArcs) > 0:
        arc = setOfArcs.pop()
        if RemoveInconsistent(obj, arc, Removed):
            for neighbour in obj.graph[arc[0]]:
                # if not obj.givenValue[neighbour]: 
                    setOfArcs.add((neighbour, arc[0]))
    return Removed

def verify(obj, getFault = False):
    for constraint in obj.AllConstraints:
        if not eval(constraint,{"value":obj.value}):
            return False
    return True