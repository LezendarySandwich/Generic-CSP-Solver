from sortedcontainers import SortedList

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
