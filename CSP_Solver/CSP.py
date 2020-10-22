import random, time, multiprocessing
from datetime import datetime
from .Util import big
from copy import deepcopy
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
    def __init__(self, variables, problem_name = 'CSP'):
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
        self.problem_name = problem_name
    
    def commonDomain(self, domain = []):
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
                self.domainHelp[i].append(value)

    def separateDomain(self, variable, domain = []):
        self.domainHelp[variable] = deepcopy(domain)
        self.domains[variable] = set(domain)

    def setValue(self, variable, value):
        self.domainHelp[variable] = [value]
        self.domains[variable] = {value}

    def add(self, comparison):
        numbers = []
        prev = False
        cur = ""
        for i in comparison:
            if i == ' ':
                continue
            if i == '[':
                prev = True
                continue
            if i == ']':
                prev = False
                numbers.append(int(cur))
                cur = ""
                continue
            if prev:
                cur += i
        comparison = compile(comparison, "<string>", "eval")
        for i in range (len(numbers)):
            n1 = numbers[i]
            for j in range(i + 1, len(numbers)):
                n2 = numbers[j];
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

    def solve_dfs(self, timeout = 10):
        self.reset()
        start = time.clock()
        BackTrack(self, timeout)
        end = time.clock()
        f = open('../Examples/dfs_Solution.txt', 'w')
        wr = self.problem_name + '\n\n'
        if end - start > timeout:
            print ("dfs timed out")
            wr += "dfs timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by dfs: ", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()

    def solve_BackTrack(self, timeout = 10):
        self.reset()
        start = time.clock()
        BackTrack(self, timeout)
        end = time.clock()
        f = open('../Examples/BackTrack_Solution.txt', 'w')
        wr = self.problem_name + '\n\n'
        if end - start > timeout:
            print ("BackTrack timed out")
            wr += "BackTrack timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by BackTrack: ", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()

    def solve_ForwardChecking(self, timeout = 10):
        self.reset()
        start = time.clock()
        ForwardChecking(self, timeout)
        end = time.clock()
        f = open('../Examples/ForwardChecking_Solution.txt', 'w')
        wr = self.problem_name + '\n\n'
        if end - start > timeout:
            print ("ForwardChecking timed out")
            wr += "ForwardChecking timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by ForwardChecking: ", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()

    def solve_ForwardChecking_MRV(self, timeout = 10):
        self.reset()
        start = time.clock()
        ForwardChecking_MRV(self, timeout)
        end = time.clock()
        f = open('../Examples/ForwardChecking_MRV_Solution.txt', 'w')
        wr = self.problem_name + '\n\n'
        if end - start > timeout:
            print ("ForwardChecking_MRV timed out")
            wr += "ForwardChecking_MRV timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by ForwardChecking_MRV: ", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()

    def solve_ForwardChecking_MRV_LCV(self, timeout = 10):
        self.reset()
        start = time.clock()
        ForwardChecking_MRV_LCV(self, timeout)
        end = time.clock()
        f = open('../Examples/ForwardChecking_MRV_LCV_Solution.txt', 'w')
        wr = self.problem_name + '\n\n'
        if end - start > timeout:
            print ("ForwardChecking_MRV_LCV timed out")
            wr += "ForwardChecking_MRV_LCV timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by ForwardChecking_MRV_LCV: ", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()
    
    def solve_HillClimbing_chooseBest(self, memoization = True, iterations = big, allowedSideMoves = None, tabuSize = 0, timeout = 10):
        self.reset()
        if allowedSideMoves == None:
            allowedSideMoves = self.variables
        start = time.clock()
        Hill_Climbing_with_restarts(obj = self, iterations=iterations, allowedSideMoves=allowedSideMoves, tabuSize=tabuSize, memoization=memoization, choice=choice.chooseBest, timeout = timeout)
        end = time.clock()
        f = open('../Examples/HillClimbing_chooseBest.txt', 'w')
        wr = self.problem_name + '\n'
        wr += "Params- memoization: " + str(memoization) + "; Allowed Number of Side Moves: " + str(allowedSideMoves) + "; Tabu List Size: " + str(tabuSize) + "; Allowed Number of iterations: " + str(iterations) + '\n\n'
        if end - start > timeout:
            print ("HillClimbing_chooseBest timed out")
            wr += "HillClimbing_chooseBest timed out"
        elif self.stop == 0:
            wr += "No valid solution exist"
        else :
            print("Time taken by HillClimbing_chooseBest:", end - start)
            for i in range(1,self.variables + 1):
                wr += "value[" + str(i) + "] : " + str(self.value[i]) + "\n"
        f.write(wr)
        f.close()

    def solve(self):
        pass
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
        # My_Algo(self)

    def createRandomInstance(self):
        for i in range(1,self.variables + 1):
            if len(self.domains[i]) == len(self.domainHelp[i]):
                self.value[i] = random.choice(self.domainHelp[i])
            else:
                self.value[i] = random.choice(list(self.domains[i]))

    def reset(self):
        self.stop = 0
        self.value = [None for i in range(self.variables + 1)]
        self.givenValue = [False for i in range(self.variables + 1)]
        self.domains = [set(self.domainHelp[i]) for i in range(self.variables + 1)]

