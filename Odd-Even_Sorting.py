# Given an array A consisting of n elements.
# Sort the even numbers in the array in ascending order, and sort the odd numbers in descending order.
#
# Print the resulting array such that the positions of even numbers and odd numbers remain the same as in the original array
# (i.e., even numbers stay in even-number positions, odd numbers stay in odd-number positions relative to the original array).
#
# Input:
# - The first line contains an integer n (1 < n ≤ 1000).
# - The next line contains n integers of the array A, all numbers are positive integers and do not exceed 1000.
#
# Output:
# - Print the resulting array after sorting, where the positions of even and odd numbers are preserved.

"""
n = int(input())
arr = list(map(int, input().split()))

even, odd = [], []
for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

even.sort()
odd.sort(reverse = True)

e, o = 0, 0
res = []
for i in range(n):
    if arr[i] % 2 == 0:
        res.append(even[e])
        e += 1
    else:
        res.append(odd[o])
        o += 1
print(*res)
"""

import sys

n = int(sys.stdin.readline())
arr = []
while len(arr) < n:
    arr.extend(map(int, sys.stdin.readline().split()))
    
even = []
odd = []
for i in arr:
    if (i & 1) == 0: # using bitwise operator to compare to last bit of each number, faster than mathematical operator
        even.append(i)
    else:
        odd.append(i)
even.sort()
odd.sort(reverse = True)
        
e = o = 0
res = [0] * n # pre-allocate, faster then append()
for i in range(n):
    if (arr[i] & 1) == 0:
        res[i] = even[e]
        e += 1
    else:
        res[i] = odd[o]
        o += 1

sys.stdout.write(" ".join(map(str, res)))