"""
testing recursive problems
"""


def test(n):
    if n >= 0:
        print(n)
        test(n - 1)


test(20)


# test fib number

def fib_bot_up(n):
    if n == 0 or n == 1:
        res = 1
    else:
        ar = [None] * (n + 1)
        ar[0] = 0
        ar[1] = 1
        for i in range(2, n + 1):
            ar[i] = ar[i - 1] + ar[i - 2]
        res = ar[n]
    return res


fib_bot_up(35)


def fib_recur(n):
    if n == 1 or n == 2:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)


fib_recur(35)
