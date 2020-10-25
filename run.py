import CSP_Solver as CS

problem_name = input('Name of Problem: ')
variables = int(input('Number of Variables: '))
genericCSP = CS.CSP(variables, problem_name=problem_name, solution_path = './Solutions/')
com = input('Do you want to have a common domain for variables(Y/N):')
if com is 'Y':
    commonDomain = [int(item) if item.isnumeric() else item for item in input("Enter values of common domain seperated by spaces: ").split()]
    genericCSP.commonDomain([i for i in range(1,100)])

while True:
    seperateDom = input('Do you want to have a seperate domain for some variable(Y/N):')
    if seperateDom is 'Y':
        separateDomain = [item for item in input("Enter values of seperate domain seperated by spaces(variable Domain): ").split()]
        genericCSP.separateDomain(separateDomain[0], separateDomain[1:])
    else: break

while True:
    seperateDom = input('Do you want to set value for some variable(Y/N):')
    if seperateDom is 'Y':
        va, val = input("Enter variable and its value separated by a space: ").split()
        genericCSP.setValue(va, val)
    else: break

numberOfConstraints = int(input('Enter number of constraints: '))

for i in range(numberOfConstraints):
    constraint = input('Enter the constraint: ')
    genericCSP.addConstraint(constraint)

timeout = int(input('Enter the timeout: '))

genericCSP.testAllDefaultParams(timeout = timeout)

for i in range(1, variables + 1):
    print('Value of variable', genericCSP.variableConversion[i], ':', genericCSP.value[i])