import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

variables = 4
mapColoring = CS.CSP(variables, problem_name='mapColoring', solution_path='./../Solutions/')
mapColoring.commonDomain(['Red', 'Blue', 'Yellow'])

mapColoring.addConstraint('value[Lucknow] is value[Delhi]')
mapColoring.addConstraint('value[Bengal] is not value[Punjab]')
mapColoring.addConstraint('value[Bengal] is not value[Delhi]')

mapColoring.testAllDefaultParams(timeout = 2)

if mapColoring.stop == 1:
    for i in range(1, variables + 1):
        print('Color of', mapColoring.variableConversion[i], ':', mapColoring.value[i])