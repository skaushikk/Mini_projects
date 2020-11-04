"""
recursion sum of array weighted by the depth, nested arrays
"""


def average(A):
    if len(A) == 1:
        return A[0]

    else:
        n = len(A)
        return (A[0] + (n - 1) * average(A[1:])) / n


A = [1, 2, 3, 4, 5, 6, 7]
print(average(A))


def weighted_sum(A):

    def helper(A, depth=1):
        _sum = 0
        for i in A:
            if isinstance(i, list):
                _sum += helper(i, depth + 1)
            else:
                _sum += i * depth
        return _sum

    return helper(A)


A = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
print(weighted_sum(A))
