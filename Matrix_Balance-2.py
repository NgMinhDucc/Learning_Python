"""
Given a square matrix of size N * N containing only positive integers.

Using the SECONDARY diagonal (the diagonal from the top-right to the bottom-left), the matrix is divided into two parts:
the upper part and the lower part relative to the SECONDARY diagonal
(excluding the elements on the SECONDARY diagonal itself).

The difference of the matrix is defined as the absolute value of:
(sum of elements in the upper part) minus (sum of elements in the lower part).

An additional integer K is given, called the balance threshold of the matrix.
If the difference is not greater than K, the matrix is considered balanced; otherwise, it is not balanced.

Your task is to compute the difference and determine whether the matrix is balanced.

Input:
- The first line contains an integer N (2 < N < 50).
- The next N lines each contain N integers representing the matrix values
  (all values are positive integers and do not exceed 1000).
- The last line contains an integer K (0 < K < 100).

Output:
- The first line prints "YES" if the matrix is balanced, otherwise "NO".
- The second line prints the computed difference of the matrix.

For example:
- Input:
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
- Output:
NO
11
"""

n = int(input())
ma = []
for i in range(n):
    arr = list(map(int, input().split()))
    ma.append(arr)
k = int(input())

upper_half = 0
lower_half = 0

for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            upper_half += ma[i][j]
        elif j > n - i - 1:
            lower_half += ma[i][j]

dif = abs(upper_half - lower_half)
print("YES" if dif <= k else "NO")
print(dif)