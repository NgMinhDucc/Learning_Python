# Given an array A[] of N elements.
# List all K-element combinations of distinct elements from A[].
# The combinations must be listed in lexicographical order:
# - Within each combination, elements are in increasing order.
# - Each combination is greater than the previous one in lexicographical order.
#
# Input:
# - The first line contains two integers N and K.
# - The second line contains N integers of array A (each value <= 1000).
# - It is guaranteed that the number of distinct elements in A is at most 20,
#   and K does not exceed 10.
#
# Output:
# - Print each valid combination on a separate line.

from itertools import combinations

n, k = map(int, input().split())
li = list(map(int, input().split()))

li = sorted(li)
# avoid duplicated elements
lis = []
for i in range(n):
    if li[i] not in lis:
        lis.append(li[i])

res = combinations(lis, k)
for com in res:
    for i in com:
        print(i, end = " ")
    print()