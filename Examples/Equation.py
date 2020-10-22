import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

variables = 3
a = CS.CSP(variables)
a.commonDomain([1,2,3,4])

a.add('value[1] + value[2] == value[3]')

a.solve()