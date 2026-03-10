"""
Given a matrix A of size N * M containing only positive integers.
Find the largest palindrome number in the matrix and all positions where this largest palindrome number appears.

Input:
- The first line contains two integers N and M (1 < N, M < 50).
- The next N lines contain the elements of the matrix.
  All values are positive integers and do not exceed 10000.

Output:
- Print the value of the largest palindrome number.
- Then print all positions where this number appears, one position per line.
  (Row index and column index are counted from 0.)
- The positions are listed in order from left to right, top to bottom.
- If no palindrome number is found, print: NOT FOUND

For example:
- Input:
6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77

- Output:
77
Vi tri [0][2]
Vi tri [3][1]
Vi tri [5][2]
Vi tri [5][3]
"""

def palindrome(n):
    return n == n[::-1]

def solve(n, m, a):
    maxx = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > 10 and palindrome(str(a[i][j])) and a[i][j] > maxx:
                maxx = a[i][j]
    
    if maxx == 0:
        print("NOT FOUND")
    else:
        print(maxx)
        for i in range(n):
            for j in range(m):
                if a[i][j] == maxx:
                    print(f"Vi tri [{i}][{j}]")

n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)

solve(n, m, a)  