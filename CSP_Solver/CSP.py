import random, time
from datetime import datetime
from .BackTrack import BackTrack
from .dfs import dfs
from .BackTrack_ordering_MRV_LCV import orderedBackTrack_MRV_LCV
from .BackTracking_MRV import orderedBackTrack_MRV
from .Hill_Climbing import HillClimbing
from .ForwardChecking import forwardChecking
from .Hill_Climbing_with_restarts import Hill_Climbing_with_restarts
from .Hill_Climbing_with_memoisation import HillClimbing_with_memoisation
class CSP:
    def __init__(self, variables):
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [[] for i in range(variables + 1)]
        self.value = [None for i in range(variables + 1)]
        self.givenValue = [False for i in range(variables + 1)]
        self.domainHelp = [[] for i in range(variables + 1)]
        self.Constraints = [[[] for i in range(variables + 1)] for j in range(variables + 1)]
        # self.Edges = set()
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
        # if [n1,n2,comparison] in self.edges:
        #     return 
        self.Constraints[n1][n2].append(comparison)
        self.Constraints[n2][n1].append(comparison)
        self.graph[n1].append([n2,comparison])
        self.graph[n2].append([n1,comparison])
        # self.edges.add([n1,n2,comparison])
        # self.edges.add([n2,n1,comparison])
    
    def solve(self):
        # start = time.time()
        # BackTrack(self)
        # end = time.time()
        # print("Time for BackTracking is :" , end - start)
        # self.reset()
        # dfs(self)
        # self.reset()
        # orderedBackTrack_MRV_LCV(self)
        # self.reset()
        # orderedBackTrack_MRV(self)
        # self.reset()
        # start = time.time()
        # HillClimbing(self)
        # end = time.time()
        # print("Time for Hill-Climbing is :" , end - start)
        # start = time.time()
        # forwardChecking(self)
        # end = time.time()
        # print("Time for ForwardChecking is :" , end - start)
        # HillClimbing_with_memoisation(self)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, memoisation=False)
        # end = time.time()
        # print("Time for Hill Climbing without memoisation is :" , end - start)
        start = time.time()
        Hill_Climbing_with_restarts(self, memoisation=True)
        end = time.time()
        print("Time for Hill Climbing with memoisation is :" , end - start)

    def createRandomInstance(self):
        random.seed(datetime.now())
        for i in range(1,self.variables + 1):
            rand = random.randint(0,len(self.domains[i])-1)
            self.value[i] = self.domainHelp[i][rand]

    def reset(self):
        self.stop = 0
        self.value = [None for i in range(self.variables + 1)]
        self.givenValue = [False for i in range(self.variables + 1)]
        self.domains = [set(self.domainHelp[i]) for i in range(self.variables + 1)]

