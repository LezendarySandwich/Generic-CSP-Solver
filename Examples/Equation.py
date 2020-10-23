import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

variables = 4
a = CS.CSP(variables, 'Equation')
a.commonDomain([1,2,3,4,5,6,7])

a.add('value[1] + value[2] + value[3] is 9')
a.add('value[2] ^ value[1] is 2')
a.add('value[3] - value[4] is 3')

a.solve_ForwardChecking_MRV_LCV()