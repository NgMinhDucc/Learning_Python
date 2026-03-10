"""
Given a matrix A of size N × M containing only positive integers.
A number is considered a lucky number if its value is exactly equal to
the difference between the largest number and the smallest number in the matrix.

In the example test, the largest value is 77 and the smallest value is 10, so the lucky value is 67.

Determine whether such a lucky number exists in the matrix.
If it exists, print all positions where it appears.

Input:
- The first line contains two integers N and M (1 < N, M < 50).
- The next N lines contain the elements of the matrix.
  All numbers are positive integers and do not exceed 10000.

Output:
- Print the lucky number if it exists.
- Then print all positions where it appears, one position per line
  (row index and column index start from 0).
- Positions are listed from left to right, top to bottom.

If no such number exists, print: NOT FOUND

For example:
- Input:
6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77

- Output:
67
Vi tri [2][1]
Vi tri [3][3]
"""

def palindrome(n):
    return n == n[::-1]

def solve(n, m, a):
    maxx, minn = 0, 100001
    for i in range(n):
        if max(a[i]) > maxx:
            maxx = max(a[i])
        if min(a[i]) < minn:
            minn = min(a[i])
    
    dif = maxx - minn
    mark = 0
    res = []
    for i in range(n):
        for j in range(m):
            if a[i][j]  == dif:
                mark = a[i][j]
                res.append(f"Vi tri [{i}][{j}]")
    
    if mark == 0:
        print("NOT FOUND")
    else:
        print(mark)
        for i in res:
            print(i)

n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

solve(n, m, a)