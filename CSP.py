import re
class CSP:
    def __init__(self, variables):
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [[] for i in range(variables + 1)]
        self.value = [0 for i in range(variables + 1)]
        self.stop = 0
    def Domain(self, domain = []):
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
    def add(self, n1, n2, comparison, t1 = None, t2 = None):
        comparison = comparison.replace(" ","")
        if t1 != None:
            comparison = comparison.replace(t1,str(n1))
        if t2 != None:
            comparison = comparison.replace(t2,str(n2))
        comparison = comparison.replace('value','self.value')
        self.graph[n1].append([n2,comparison])
    def solve(self, cur):
        if self.stop:
            return 
        if cur > self.variables:
            self.stop = 1
            print(self.value[1:self.variables+1])
            return
        for value in self.domains[cur]:
            self.value[cur] = value
            Removed = []
            for neighbour in self.graph[cur]:
                for Nval in self.domains[neighbour[0]]:
                    self.value[neighbour[0]] = Nval
                    if not eval(neighbour[1]):
                        Removed.append((neighbour[0], Nval))
            for rem in Removed:
                self.domains[rem[0]].discard(rem[1])
            self.solve(cur + 1)
            for rem in Removed:
                self.domains[rem[0]].add(rem[1])
    def reset(self):
        self.stop = 0
        self.value = [0 for i in range(variables + 1)]

def constraints(self):
    for i in range(1,self.variables+1):
        for j in range(i+1,self.variables+1):
            self.add(i,j,'value[i] != value[j]','i','j')
            self.add(i,j,'abs(value[j] - value[i]) != j - i','i','j')

CSP.constraints = constraints
n = 4
a = CSP(n)
dom = []
for i in range (n):
    dom.append(i + 1)
a.Domain(dom)
a.constraints()
a.solve(1)
