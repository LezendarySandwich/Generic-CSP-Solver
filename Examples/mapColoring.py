import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

variables = 8
mapColoring = CS.CSP(variables, problem_name='mapColoring', solution_path='./../Solutions/')
mapColoring.commonDomain(['Red', 'Blue', 'Yellow', 'Indigo', 'Pink', 'Black', 'White', 'Orange'])

for i in range(1,variables + 1):
    for j in range(i + 1, variables + 1):
        mapColoring.addConstraint('value[' + str(i) + '] is not value[' + str(j) + ']')

mapColoring.addConstraint('value[1] is not value[8]')
mapColoring.setValue(8, 'Blue')

mapColoring.testAllDefaultParams(timeout = 2)

if mapColoring.stop == 1:
    for i in range(1, variables + 1):
        print('Color of city', i, ':', mapColoring.value[i])