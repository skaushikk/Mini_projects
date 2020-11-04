"""

given an array,
1. return min. pairs
2. return indices i and J so that |Ai - Aj| is minimum
"""
def arr_min(A):
    A_sorted = sorted(A)
    ans=[]
    _min = 2**31
    for i in range(len(A)-1):
        dif = abs(A[i+1]-A[i])
        if dif < _min:
            _min = dif
            ans = [[A[i], A[i+1]]]
        elif dif==_min:
            ans.append([A[i], A[i+1]])
    return ans

def arr_min_idx_BF(A):
    D = []
    _min=2**31
    for i, num in enumerate(A):
        for j in range(i+1, len(A)):
            dif = abs(num-A[j])
            if dif < _min:
                _min=dif
                D=[[i,j]]
            elif dif == _min:
                D.append([[i,j]])

    return D

# A=[2,4,5,7,9,1, 6]
# print(arr_min_idx_BF(A))

"""
Kadane's Algorithm b- find the max. sum of the subarray
"""

def kadanes(A):
    max_global = A[0]
    max_cur = A[0]
    for i in range(1 ,len(A)):
        max_cur = max(max_cur+ A[i],A[i] )
        if max_cur > max_global:
            max_global = max_cur
    return max_global

A = [-2, 3, 2,-1]
print(kadanes(A))
