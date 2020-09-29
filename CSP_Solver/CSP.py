import sys
sys.path.append(".")
import random
from datetime import datetime
from . import BackTrack
class CSP:
    def __init__(self, variables):
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [[] for i in range(variables + 1)]
        self.value = [0 for i in range(variables + 1)]
        self.domainHelp = [[] for i in range(variables + 1)]
        self.stop = 0
    def Domain(self, domain = []):
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
                self.domainHelp[i].append(value)
    def add(self, n1, n2, comparison, t1 = None, t2 = None):
        comparison = comparison.replace(" ","")
        if t1 != None:
            comparison = comparison.replace(t1,str(n1))
        if t2 != None:
            comparison = comparison.replace(t2,str(n2))
        comparison = comparison.replace('value','obj.value')
        self.graph[n1].append([n2,comparison])
    def solve(self):
        BackTrack.BackTrack(self, 1)
    def createRandomInstance(self):
        random.seed(datetime.now())
        Instance = [-1]
        for i in range(1,self.variables + 1):
            rand = random.randint(0,len(self.domains[i])-1)
            Instance.append(self.domainHelp[i][rand])
        return Instance
    def reset(self):
        self.stop = 0
        self.value = [0 for i in range(variables + 1)]

