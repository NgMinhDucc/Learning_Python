# Given an array A consisting of N elements.
#
# An inversion is a pair of indices (u, v) such that u < v and A[u] > A[v].
# Your task is to count the number of inversions in the given array A.
#
# Input:
# - The first line contains an integer N (N ≤ 1000), the number of elements in the array.
# - The second line contains N integers A[i] (1 ≤ A[i] ≤ 10^9).
#
# Output:
# - Print a single integer representing the number of inversions found in the array.
#
# For example:
# Input:
# 5
# 2 4 1 3 5
# Output: 3 (since we have 3 pairs: (2, 1), (4,1) and (4, 3)).

n = int(input())
a = list(map(int, input().split()))
res = [0] * 2
final_res = []

def dem():
    if res[0] > res[1]:
        final_res.append(res)
    

def Try(i, pos):
    for j in range(pos, n - 2 + i + 1):
        res[i] = a[j]
        if i == 1:
            dem()
        else:
            Try(i + 1, j + 1)
            
Try(0, 0)
print(len(final_res))

"""
More optimized and Pythonic

from itertools import combinations

n = int(input())
a = list(map(int, input().split()))
k = 2
res = combinations(a, k)
cnt = 0
for com in res:
    if com[0] > com[1]:
        cnt += 1
print(cnt)
"""