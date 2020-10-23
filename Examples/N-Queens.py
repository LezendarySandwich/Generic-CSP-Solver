import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

n = 30
N_Queens = CS.CSP(n, problem_name='N-Queens')
N_Queens.commonDomain([i for i in range(1,n + 1)])

for i in range(1,N_Queens.variables+1):
    for j in range(i+1,N_Queens.variables+1):
        N_Queens.addConstraint('value['+str(i)+'] != value['+str(j)+']')
        N_Queens.addConstraint('abs(value['+str(j)+'] - value['+str(i)+']) != '+str(j)+'-'+str(i))

N_Queens.testAllDefaultParams(timeout = 2)

if N_Queens.stop == 1:
    for val in range(1,n + 1):
        print('|', sep='', end='')
        for va in range(1,n + 1):
            if val == N_Queens.value[va]:
                print('Q', end='')
            else :
                print('.', end='')
            print('|', sep='', end='')
        print();
