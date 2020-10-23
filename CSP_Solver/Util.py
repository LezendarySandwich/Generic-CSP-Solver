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
    if not obj.multivariate:
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
    else:
        for value in obj.domains[cur]:
            obj.value[cur] = value
            curr = 0
            for constraint, neighbours in obj.multivariateGraph[cur]:
                left, remaining = len(neighbours), -1
                for neighbour in neighbours:
                    left -= 1 if obj.givenValue[neighbour] else 0
                    remaining = remaining if obj.givenValue[neighbour] else neighbour
                if left is 1:
                    for val in obj.domains[remaining]:
                        obj.value[remaining] = val
                        curr += 1 if not eval(constraint, {"value": obj.value}) else 0
            Values.append((curr, value))
    Values.sort()
    return Values

def toRemove(obj, cur, value):
    Removed = []
    obj.value[cur] = value
    if not obj.multivariate:
        for neighbour in obj.graph[cur]:
            if obj.givenValue[neighbour]:
                continue
            for Nval in obj.domains[neighbour]:
                obj.value[neighbour] = Nval
                for constraint in obj.graphConstraints[cur][neighbour]:
                    if not eval(constraint,{"value":obj.value}):
                        Removed.append((neighbour, Nval))
                        break
    else:
        for constraint, neighbours in obj.multivariateGraph[cur]:
            left = len(neighbours)
            remaining = -1
            for neighbour in neighbours:
                left -= 1 if obj.givenValue[neighbour] else 0
                remaining = remaining if obj.givenValue[neighbour] else neighbour
            if left is 1:
                for val in obj.domains[remaining]:
                    obj.value[remaining] = val
                    if not eval(constraint, {"value": obj.value}):
                        Removed.append((remaining, val))
    return Removed

def verify(obj, getFault = False):
    for constraint in obj.AllConstraints:
        if not eval(constraint,{"value":obj.value}):
            return False
    return True