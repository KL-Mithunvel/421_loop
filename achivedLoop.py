from num_op import *

def enterLoop(lis):
    n = lis[-1]
    next_n = calc(n)
    while n != next_n:
        lis.append(next_n)
        print(lis[-1])
        next_n = calc(lis[-1])
