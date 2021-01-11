import random, time
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
from .Genetic_Algo.Genetic_Solver import Genetic_Solver
from .General_LocalSearch_Algorithms.local_beam_search import local_beam_search
from .General_LocalSearch_Algorithms.Simulated_Annealing import simulated_annealing
from .ArcConsistency.Arc_Consistent_Backtracking import ArcConsistent_MRV_LCV
from .Novel_Approach.My_Algorithm import My_Algo

class CSP:
    def __init__(self, variables, solution_path = None, problem_name = 'CSP'):
        random.seed(datetime.now())
        self.variables = variables
        self.domains = [set() for i in range(variables + 1)]
        self.graph = [set() for i in range(variables + 1)]
        self.value = [None for i in range(variables + 1)]
        self.givenValue = [False for i in range(variables + 1)]
        self.domainHelp = [[] for i in range(variables + 1)]
        self.graphConstraints = [dict() for i in range(variables + 1)]
        self.multivariateGraph = [[] for i in range(variables + 1)]
        self.AllConstraints = []
        self.stop = 0
        self.problem_name = problem_name
        self.multivariate = False
        self.currentHelp = 1
        self.variableConversion = dict()
        for i in range(1,variables + 1):
            self.variableConversion[i] = i
        if solution_path: self.solution_path = solution_path
    
    def commonDomain(self, domain = []):
        """
        To set same domain for all variables
        """
        for value in domain:
            for i in range(1,self.variables+1):
                self.domains[i].add(value)
                self.domainHelp[i].append(value)

    def separateDomain(self, variable, domain = []):
        """
        To separately set domain values for variables
        """
        self.domainHelp[self.variableConversion[variable]] = deepcopy(domain)
        self.domains[self.variableConversion[variable]] = set(domain)

    def setValue(self, variable, value):
        """
        To Enforce Unary Constraints
        """
        self.domainHelp[self.variableConversion[variable]] = [value]
        self.domains[self.variableConversion[variable]] = {value}

    def addConstraint(self, constraint):
        """
        Enforce constraints
        pass comparison as string
        """
        numbers, prev, cur = [], False, ""
        for i in constraint:
            if i == ' ':
                continue
            if i == '[':
                prev = True
                continue
            if i == ']':
                prev = False
                if not cur.isnumeric() and cur not in self.variableConversion:
                    print(cur, self.currentHelp)
                    self.variableConversion[cur] = self.currentHelp
                    self.variableConversion[self.currentHelp] = cur
                    self.currentHelp += 1
                elif cur.isnumeric(): 
                    self.variableConversion[cur] = int(cur)
                    self.variableConversion[int(cur)] = int(cur)
                numbers.append(self.variableConversion[cur])
                cur = ""
                continue
            if prev:
                cur += i
        for key in self.variableConversion:
            if str(key).isnumeric(): continue
            constraint = constraint.replace(str(key), str(self.variableConversion[key]))
        constraint = compile(constraint, "<string>", "eval")
        if len(numbers) > 2:
            self.multivariate = True
        for i in range (len(numbers)):
            n1 = numbers[i]
            for j in range(i + 1, len(numbers)):
                n2 = numbers[j];
                self.multivariateGraph[n1].append((constraint, numbers))
                self.multivariateGraph[n2].append((constraint, numbers))
                if n2 in self.graphConstraints[n1]:
                    self.graphConstraints[n1][n2].add(constraint)
                else:
                    self.graphConstraints[n1][n2] = {constraint}
                if n1 in self.graphConstraints[n2]:
                    self.graphConstraints[n2][n1].add(constraint)
                else:
                    self.graphConstraints[n2][n1] = {constraint}
                self.graph[n1].add(n2)
                self.graph[n2].add(n1)
        self.AllConstraints.append(constraint)

    def solve_dfs(self, timeout = 10):
        self.reset()
        start = time.time()
        dfs(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'dfs_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("dfs timed out")
                wr += "dfs timed out"
            elif self.stop == 0:
                print("DFS: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by dfs: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_BackTrack(self, timeout = 10):
        self.reset()
        start = time.time()
        BackTrack(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'BackTrack_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("BackTrack timed out")
                wr += "BackTrack timed out"
            elif self.stop == 0:
                print("BackTrack: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by BackTrack: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_ForwardChecking(self, timeout = 10):
        self.reset()
        start = time.time()
        ForwardChecking(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ForwardChecking_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("ForwardChecking timed out")
                wr += "ForwardChecking timed out"
            elif self.stop == 0:
                print("Forward Checking: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by ForwardChecking: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_ForwardChecking_MRV(self, timeout = 10):
        self.reset()
        start = time.time()
        ForwardChecking_MRV(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ForwardChecking_MRV_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("ForwardChecking_MRV timed out")
                wr += "ForwardChecking_MRV timed out"
            elif self.stop == 0:
                print("Forward Checking MRV: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by ForwardChecking_MRV: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_ForwardChecking_MRV_LCV(self, timeout = 10):
        self.reset()
        start = time.time()
        ForwardChecking_MRV_LCV(self, timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ForwardChecking_MRV_LCV_Solution.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("ForwardChecking_MRV_LCV timed out")
                wr += "ForwardChecking_MRV_LCV timed out"
            elif self.stop == 0:
                print("Forward Checking MRV and LCV: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by ForwardChecking_MRV_LCV: ", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()
    
    def solve_HillClimbing_chooseBest(self, memoization = True, iterations = big, allowedSideMoves = None, tabuSize = 0, timeout = 10):
        self.reset()
        if allowedSideMoves == None:
            allowedSideMoves = self.variables << 1
        start = time.time()
        Hill_Climbing_with_restarts(obj = self, iterations=iterations, allowedSideMoves=allowedSideMoves, tabuSize=tabuSize, memoization=memoization, choice=choice.chooseBest, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'HillClimbing_chooseBest.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- memoization: " + str(memoization) + "; Allowed Number of Side Moves: " + str(allowedSideMoves) + "; Tabu List Size: " + str(tabuSize) + "; Allowed Number of iterations: " + str(iterations) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("HillClimbing_chooseBest timed out")
                wr += "HillClimbing_chooseBest timed out"
            elif self.stop == 0:
                print("HillClimbing_chooseBest: No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by HillClimbing_chooseBest:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_HillClimbing_greedyBias(self, memoization = True, iterations = big, allowedSideMoves = None, tabuSize = 0, timeout = 10):
        self.reset()
        if allowedSideMoves == None:
            allowedSideMoves = self.variables << 1
        start = time.time()
        Hill_Climbing_with_restarts(obj = self, iterations=iterations, allowedSideMoves=allowedSideMoves, tabuSize=tabuSize, memoization=memoization, choice=choice.greedyBias, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'HillClimbing_greedyBias.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- memoization: " + str(memoization) + "; Allowed Number of Side Moves: " + str(allowedSideMoves) + "; Tabu List Size: " + str(tabuSize) + "; Allowed Number of iterations: " + str(iterations) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("HillClimbing_greedyBias timed out")
                wr += "HillClimbing_greedyBias timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by HillClimbing_greedyBias:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_HillClimbing_chooseRandom(self, memoization = True, iterations = big, allowedSideMoves = None, tabuSize = 0, timeout = 10):
        self.reset()
        if allowedSideMoves == None:
            allowedSideMoves = self.variables << 1
        start = time.time()
        Hill_Climbing_with_restarts(obj = self, iterations=iterations, allowedSideMoves=allowedSideMoves, tabuSize=tabuSize, memoization=memoization, choice=choice.chooseRandom, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'HillClimbing_chooseRandom.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- memoization: " + str(memoization) + "; Allowed Number of Side Moves: " + str(allowedSideMoves) + "; Tabu List Size: " + str(tabuSize) + "; Allowed Number of iterations: " + str(iterations) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("HillClimbing_chooseRandom timed out")
                wr += "HillClimbing_chooseRandom timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by HillClimbing_chooseRandom:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_GeneticAlgo(self, populationSize = None, generations = big, timeout = 10):
        self.reset()
        if populationSize == None:
            populationSize = self.variables << 1
        start = time.time()
        Genetic_Solver(obj = self, populationSize = populationSize, generations = generations, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'GeneticAlgorithm.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- Size of Population: " + str(populationSize) + "; Allowed Number of Generations " + str(generations) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("Genetic Algorithm timed out")
                wr += "Genetic Algorithm timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by Genetic Algorithm:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_local_beam_search(self, beams = None, timeout = 10):
        self.reset()
        if beams == None:
            beams = self.variables << 1
        start = time.time()
        local_beam_search(obj = self, k = beams, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'local_beam_search.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- Number of beams: " + str(beams) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("local beam search timed out")
                wr += "local beam search timed out"
            elif self.stop == 0:
                print("Solution not found using local beam search")
                wr += "Solution not found"
            else :
                print("Time taken by local beam search:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_Simulated_Annealing(self, iterations = big, initialTemperature = 10000, cooling_coefficient = 1, timeout = 10):
        self.reset()
        start = time.time()
        while time.time() - start < timeout:
            simulated_annealing(obj = self, iterations=iterations, temperature=initialTemperature, decreaseConstant=cooling_coefficient, timeout = timeout)
            if self.stop == 1: break
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'Simulated_Annealing.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- Initial Temperature: " + str(initialTemperature) + '; Cooling Coeffecient: ' + str(cooling_coefficient) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("Simulated Annealing timed out")
                wr += "Simulated Annealing timed out"
            elif self.stop == 0:
                print("Solution not found using Simulated Annealing")
                wr += "Solution not found"
            else :
                print("Time taken by Simulated Annealing:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_ArcConsistent_BackTracking(self, timeout = 10):
        self.reset()
        start = time.time()
        ArcConsistent_MRV_LCV(obj = self, timeout = timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'ArcConsistent_BackTracking.txt', 'w')
            wr = self.problem_name + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("Arc Consistent BackTracking timed out")
                wr += "Arc Consistent BackTracking timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by Arc Consistent BackTracking:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def solve_novelAlgorithm(self, split = None, allowedSideMoves = None, tabuSize = 0, tries = None, timeout = 10):
        self.reset()
        if tries is None: tries = self.variables * 3
        if allowedSideMoves is None: allowedSideMoves = self.variables << 1
        start = time.time()
        My_Algo(obj = self, split=split, allowedSideMoves=allowedSideMoves, tabuSize=tabuSize, tries = tries, timeout=timeout)
        end = time.time()
        if hasattr(self, 'solution_path'):
            f = open(self.solution_path + 'novelAlgorithm.txt', 'w')
            wr = self.problem_name + '\n'
            wr += "Params- Split: " + str(split) + '; Allowed Number of Side Moves: ' + str(allowedSideMoves) + '; Size of Tabu List: ' + str(tabuSize) + '\n'
            wr += 'Time Taken: ' + str(end - start) + '\n\n'
            if end - start > timeout:
                print ("Novel Algorithm timed out")
                wr += "Novel Algorithm BackTracking timed out"
            elif self.stop == 0:
                print("No valid solution exist")
                wr += "No valid solution exist"
            else :
                print("Time taken by Novel Algorithm:", end - start)
                for i in range(1,self.variables + 1):
                    wr += "value[" + str(self.variableConversion[i]) + "] : " + str(self.value[i]) + "\n"
            f.write(wr)
            f.close()

    def testAllDefaultParams(self, timeout = 10):
        self.solve_dfs(timeout = timeout)
        self.solve_BackTrack(timeout = timeout)
        self.solve_ForwardChecking(timeout = timeout)
        self.solve_ForwardChecking_MRV(timeout = timeout)
        self.solve_ForwardChecking_MRV_LCV(timeout = timeout)
        if not self.multivariate:
            self.solve_HillClimbing_chooseBest(timeout = timeout)
            self.solve_HillClimbing_chooseRandom(timeout = timeout)
            self.solve_HillClimbing_greedyBias(timeout = timeout)
            self.solve_GeneticAlgo(timeout = timeout)
            self.solve_local_beam_search(timeout = timeout)
            self.solve_Simulated_Annealing(timeout = timeout)
            self.solve_ArcConsistent_BackTracking(timeout = timeout)
            self.solve_novelAlgorithm(timeout = timeout)

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