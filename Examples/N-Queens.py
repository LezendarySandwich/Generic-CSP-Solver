import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

n = 10
a = CS.CSP(n, problem_name='N-Queens')
a.commonDomain([i for i in range(1,n + 1)])

for i in range(1,a.variables+1):
    for j in range(i+1,a.variables+1):
        a.add('value['+str(i)+'] != value['+str(j)+']')
        a.add('abs(value['+str(j)+'] - value['+str(i)+']) != '+str(j)+'-'+str(i))

a.solve_BackTrack(timeout = 2)

if a.stop == 1:
    for val in range(1,n + 1):
        print('|', sep='', end='')
        for va in range(1,n + 1):
            if val == a.value[va]:
                print('Q', end='')
            else :
                print('.', end='')
            print('|', sep='', end='')
        print();
