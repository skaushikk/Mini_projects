from util import time_it
import time


@time_it
def factorial(num):
    X = k = num
    while k > 1:
        X = X * (k - 1)
        k = k - 1
    return X


def factorial_recursion(num):
    if num == 1:
        return 1

    return num * factorial_recursion(num - 1)


if __name__ == '__main__':
    print(factorial_recursion(10))

"""
reverse a string
"""
import sys

sys.setrecursionlimit(10**6)


# Implement a recursive reverse function
def reverse_str(str):
    # print (str)
    # Check for the base case at the end there will be at least one char
    if len(str) <= 1:
        return str

        # Implement recursive reverse
        # Take first index of the string and then add rest starts from index 1 and do a recursive call
        return reverse_str(str[1:] + str[0])

    # Test


print(reverse_str('hello world'))
