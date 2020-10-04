# import copy
# a = [(1,4), (1,2), (1,3)]
# # a = [0 if a[i] <= 3 else a[i] for i in range(0,len(a) - 1)]
# a.sort(key = lambda x: x[0])
# print(a)

# def bruh():
#     return 1 , 2

# a = [1,2,3,4,5]
# a.extend(bruh())
# print(a)

import random

def func(a):
    a = [random.randint(1,4) if i is not 0 and random.uniform(0,1) <= 0.5 else a[i] for i in range(4)]
    return a

a = [0,[1,2,3,4]]
b = func(a[1])
# b = [1,2,3,4]
# c = a[:2] + b[2:]
print(b)