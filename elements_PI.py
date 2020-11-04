import psutil
import os
from memory_profiler import profile

# @profile(precision=4)
def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

def even_odd_recur(A):
    def helper(A, next_even, next_odd):
        if A[next_odd] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
        helper(A, next_even, next_odd)
    helper(A, next_even=0, next_odd=len(A)-1)
    return A

# @profile(precision=4)
def even_odd_reg(A):
    Aeven = []
    Aodd = []

    for i in A:
        if i % 2 == 0:
            Aeven.append(i)
        else:
            Aodd.append(i)
    A = Aeven + Aodd
    return A

A= list(range(10000))
# print(even_odd_reg(A))
# print(even_odd(A))
print(even_odd_recur(A))