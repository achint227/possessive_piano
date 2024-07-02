"""
In this problem, you are given an integer N, and a permutation,
P of the integers from 1 to N, denoted as (a_1, a_2, ..., a_N).
You want to rearrange the elements of the permutation into increasing order,
repeatedly making the following operation:
Select a sub-portion of the permutation, (a_i, ..., a_j), and reverse its order.
Your goal is to compute the minimum number of such operations
required to return the permutation to increasing order.
"""

def getNeighbors(arr):

    res = []
    for i in range(0, len(arr)):
        for j in range(i + 2, len(arr) + 1):
            new = arr[:]
            new[i:j] = list(reversed(new[i:j]))
            res.append(new)
    return res


print(getNeighbors(list(range(1, 6))))
