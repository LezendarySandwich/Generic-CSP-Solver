import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

variables = 10
Equation = CS.CSP(variables, problem_name='Equation',solution_path='./../Solutions/')
Equation.commonDomain([i for i in range(1,100)])

Equation.addConstraint('value[1] + value[2] + value[3] is 9')
Equation.addConstraint('value[2] ^ value[1] is 2')
Equation.addConstraint('value[3] - value[4] is 3')
Equation.addConstraint('value[1] - 2 * value[2] + value[5] is value[7]')
Equation.addConstraint('value[7] ^ value[6] == value[4]')
Equation.addConstraint('value[6] - 5 * value[7] + 4 * value[3] == value[1] * value[4]')
Equation.addConstraint('value[7] - value[2] is not value[4]')
Equation.addConstraint('value[7] + value[2] >= value[5]')
Equation.addConstraint('value[8] + value[9] > value[10]')
Equation.setValue(10, 60)
Equation.addConstraint('value[8] - value[9] + value[4] < value[10] + 2 * value[5]')
Equation.addConstraint('value[8] ^ value[9] + value[4] is value[10]')
Equation.addConstraint('(value[8] & value[9]) | value[4] < value[10] - 5 * value[3]')
Equation.addConstraint('value[1] * value[2] // value[3] < value[7]')

Equation.testAllDefaultParams(timeout = 5)

for i in range(1, variables + 1):
    print('Value of variable', i, ':', Equation.value[i])