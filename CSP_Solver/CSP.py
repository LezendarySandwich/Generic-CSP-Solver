import random, time
from datetime import datetime
from .Trivial_Algorithms.BackTrack import BackTrack
from .Trivial_Algorithms.dfs import dfs
from .Forward_Checking.ForwardChecking import ForwardChecking
from .Forward_Checking.ForwardChecking_MRV import ForwardChecking_MRV
from .Forward_Checking.ForwardChecking_MRV_LCV import ForwardChecking_MRV_LCV
from .Hill_Climbing.Hill_Climbing_Util import choice
from .Hill_Climbing.Hill_Climbing_with_restarts import Hill_Climbing_with_restarts
from .Hill_Climbing.Hill_Climbing import HillClimbing
from .Genetic_Algo.Genetic_Solver import Genetic_Solver
from .General_LocalSearch_Algorithms.local_beam_search import local_beam_search
from .General_LocalSearch_Algorithms.Simulated_Annealing import simulated_annealing
from .Arc_Consistent_Backtracking import ArcConsistent_MRV_LCV
from .My_Algorithm import My_Algo

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
    def commonDomain(self, domain = []):
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
        # BackTrack(self)
        # self.reset()
        # dfs(self)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, iterations=200, allowedSideMoves=200, tabuSize=20, memoization=False, choice=choice.greedyBias)
        # end = time.time()
        # self.reset()
        # print("Time for Hill Climbing Tabu search is :" , end - start)
        # start = time.time()
        # Hill_Climbing_with_restarts(self, iterations=200, allowedSideMoves=200, tabuSize=50, memoization=True, choice=choice.chooseBest)
        # end = time.time()
        # self.reset()
        # print("Time for Hill Climbing Tabu search is :" , end - start)
        # Genetic_Solver(self, 400, 200)
        # start = time.time()
        # ForwardChecking_MRV(self)
        # print(time.time() - start)
        # local_beam_search(self, 100)
        # simulated_annealing(obj = self)
        # ForwardChecking_MRV(self)
        # ArcConsistent_MRV_LCV(self)
        My_Algo(self)

    def createRandomInstance(self):
        for i in range(1,self.variables + 1):
            self.value[i] = random.choice(list(self.domains[i]))

    def reset(self):
        self.stop = 0
        self.value = [None for i in range(self.variables + 1)]
        self.givenValue = [False for i in range(self.variables + 1)]
        self.domains = [set(self.domainHelp[i]) for i in range(self.variables + 1)]

