from copy import deepcopy 
from CSP_Solver.Util import big
import random

class Instance:
    def __init__(self, obj, known):
        self.value = deepcopy(obj.value)
        self.Faults = [dict() for i in range(obj.variables + 1)]
        self.defaultFaults(obj, known)
        self.currentFitness = self.fitness()

    def fitness(self):
        fit = 0
        for i in range(1,len(self.value)):
            fit += self.Faults[i][self.value[i]]
        return fit

    def writeFaults(self, obj, cur, known, add = 1):
        if (cur, self.value[cur]) in known:
            for (va, value) in known[(cur, self.value[cur])]:
                self.Faults[va][value] += add
        else:
            Vl = []
            for va in obj.graph[cur]:
                previousVal = self.value[va]
                for value in obj.domains[va]:
                    self.value[va] = value
                    for constraint in obj.graphConstraints[cur][va]:
                        if not eval(constraint,{"value":self.value}):
                            self.Faults[va][value] += add
                            Vl.append((va, value))
                            break
                self.value[va] = previousVal
            known[(cur, self.value[cur])] = Vl

    def deleteFaults(self, obj, cur, known):
        self.writeFaults(obj, cur, known, -1)

    def changeVal(self, obj, cur, newVal, known):
        self.currentFitness += (self.Faults[cur][newVal] - self.Faults[cur][self.value[cur]]) << 1
        self.deleteFaults(obj, cur, known)
        self.value[cur] = newVal
        self.writeFaults(obj, cur, known)

    def defaultFaults(self, obj, known):
        for i in range(1,obj.variables + 1):
            for value in obj.domainHelp[i]:
                self.Faults[i][value] = 0
        for i in range(1,obj.variables + 1):
            self.writeFaults(obj, i, known)
    
    def bestNeighbours(self, obj, index):
        neighbour = []
        # fitness Value, variable to be changed, value to be changed to
        for i in range(1,len(self.value)):
            mn, val = big, []
            for j in obj.domainHelp[i]:
                if mn > self.Faults[i][j] - self.Faults[i][self.value[i]]:
                    mn = self.Faults[i][j] - self.Faults[i][self.value[i]]
                    val = [j]
                elif mn == self.Faults[i][j] - self.Faults[i][self.value[i]]:
                    val.append(j)
            if mn < 0:
                neighbour.append((self.currentFitness + 2 * mn, index, i, random.choice(val)))
        return neighbour
    
    def randNeighbour(self, obj):
        va = random.randint(1, len(self.value) - 1)
        val = random.choice(obj.domainHelp[va])
        delta = self.Faults[va][val] - self.Faults[va][self.value[va]]
        return va, val, delta

    def ver(self):
        for i in range(1,len(self.value)):
            if self.Faults[i][self.value[i]] is not 0:
                return False
        if self.currentFitness is not 0:
            raise Exception("Wrong Code")
        return True