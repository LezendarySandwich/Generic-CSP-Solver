import random, time
from datetime import datetime
from .BackTrack import BackTrack
from .dfs import dfs
from .BackTrack_ordering_MRV_LCV import orderedBackTrack_MRV_LCV
from .BackTracking_MRV import orderedBackTrack_MRV
from .Hill_Climbing import HillClimbing
from .ForwardChecking import forwardChecking
from .Hill_Climbing_with_restarts import Hill_Climbing_with_restarts, choice
from .Hill_Climbing_with_memoisation import HillClimbing_with_memoisation
from .Hill_Climbing_choose_random_with_memoisation import HillClimbing_choose_random_with_memoisation
from .Hill_Climbing_greedyBias_with_memoisation import HillClimbing_greedyBias_with_memoisation

class CSP:
    def __init__(self, variables):
        random.seed(datetime.now())
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [set() for i in range(variables + 1)]
        self.value = [None for i in range(variables + 1)]
        self.givenValue = [False for i in range(variables + 1)]
        self.domainHelp = [[] for i in range(variables + 1)]
        self.graphConstraints = [dict() for i in range(variables + 1)]
        self.AllConstraints = []
        self.stop = 0
    def Domain(self, domain = []):
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
                self.domainHelp[i].append(value)
    def add(self, n1, n2, comparison, t1 = None, t2 = None):
        if t1 != None:
            comparison = comparison.replace(t1,str(n1))
        if t2 != None:
            comparison = comparison.replace(t2,str(n2))
        # comparison = comparison.replace('value','obj.value')
        comparison = compile(comparison, "<string>", "eval")
        if n2 in self.graphConstraints[n1]:
            self.graphConstraints[n1][n2].add(comparison)
        else:
            self.graphConstraints[n1][n2] = {comparison}
        if n1 in self.graphConstraints[n2]:
            self.graphConstraints[n2][n1].add(comparison)
        else:
            self.graphConstraints[n2][n1] = {comparison}
        self.graph[n1].add(n2)
        self.graph[n2].add(n1)
        self.AllConstraints.append(comparison)

    def solve(self):
        # start = time.time()
        # BackTrack(self)
        # end = time.time()
        # self.reset()
        # print("Time for BackTracking is :" , end - start)
        # dfs(self)
        # self.reset()
        # start = time.time()
        # orderedBackTrack_MRV_LCV(self)
        # end = time.time()
        # print("Time for BackTracking with MRV and LCV is :" , end - start)
        # self.reset()
        # start = time.time()
        # orderedBackTrack_MRV(self)
        # end = time.time()
        # print("Time for BackTracking with MRV is :" , end - start)
        # self.reset()
        # start = time.time()
        # HillClimbing(self)
        # end = time.time()
        # print("Time for Hill-Climbing is :" , end - start)
        # self.reset()
        # start = time.time()
        # forwardChecking(self)
        # self.reset()
        # end = time.time()
        # print("Time for ForwardChecking is :" , end - start)
        # HillClimbing_with_memoisation(self)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, memoisation=False, allowedSideMoves = 20)
        # end = time.time()
        # print("Time for Hill Climbing without memoisation is :" , end - start)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, memoisation=True, allowedSideMoves=200)
        # end = time.time()
        # print("Time for Hill Climbing with memoisation is :" , end - start)
        # HillClimbing_choose_random_with_memoisation(self)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, memoisation=True, allowedSideMoves=250, choice=choice.greedyBias)
        # end = time.time()
        # print("Time for Hill Climbing with memoisation is :" , end - start)
        # HillClimbing_greedyBias_with_memoisation(self)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, memoisation=True, allowedSideMoves=250,tabuSize=200, iterations = 300)
        # end = time.time()
        # print("Time for Hill Climbing with memoisation is :" , end - start)
        start = time.time()
        Hill_Climbing_with_restarts(self, memoisation=True, allowedSideMoves=400,tabuSize=20, iterations = 500, choice=choice.chooseRandom)
        end = time.time()
        print("Time for Hill Climbing with memoisation is :" , end - start)

    def createRandomInstance(self):
        for i in range(1,self.variables + 1):
            rand = random.randint(0,len(self.domains[i])-1)
            self.value[i] = self.domainHelp[i][rand]

    def reset(self):
        self.stop = 0
        self.value = [None for i in range(self.variables + 1)]
        self.givenValue = [False for i in range(self.variables + 1)]
        self.domains = [set(self.domainHelp[i]) for i in range(self.variables + 1)]

