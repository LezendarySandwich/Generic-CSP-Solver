import sys
sys.path.insert(0, './../')
# from CSP_Solver.CSP import CSP
import CSP_Solver as CS

def constraints(self):
    for i in range(1,self.variables+1):
        for j in range(i+1,self.variables+1):
            self.add(i,j,'value[i] != value[j]','i','j')
            self.add(i,j,'abs(value[j] - value[i]) != j - i','i','j')

CS.CSP.constraints = constraints
n = 200
a = CS.CSP(n)
dom = []
for i in range (n):
    dom.append(i + 1)
a.Domain(dom)
a.constraints()
a.solve()