import sys
sys.path.insert(0, './../')
import CSP_Solver as CS

n = 50
a = CS.CSP(n)
dom = []
for i in range (n):
    dom.append(i + 1)
a.commonDomain(dom)

for i in range(1,a.variables+1):
    for j in range(i+1,a.variables+1):
        a.add('value['+str(i)+'] != value['+str(j)+']')
        a.add('abs(value['+str(j)+'] - value['+str(i)+']) != '+str(j)+'-'+str(i))

a.solve_HillClimbing_chooseBest()

for val in range(1,n + 1):
    print('|', sep='', end='')
    for va in range(1,n + 1):
        if val == a.value[va]:
            print('Q', end='')
        else :
            print('.', end='')
        print('|', sep='', end='')
    print();
