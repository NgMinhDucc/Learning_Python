"""
Given a matrix A of size N * M containing only positive integers.
If N ≠ M, transform matrix A into a square matrix using the following rules:
- If N > M, remove rows with odd indices (row numbering starts from 1) from the original matrix until N = M.
  Example: N = 6, M = 4 → remove row 1 and row 3.
- If M > N, remove columns with even indices (column numbering starts from 1) from the original matrix until N = M.
  Example: N = 4, M = 6 → remove column 2 and column 4.
After the transformation, print the resulting square matrix.

Input:
- The first line contains two integers N and M (1 < N, M < 50).
- The next N lines contain the elements of matrix A.
  All values are positive integers and do not exceed 1000.

Output:
- Print the resulting square matrix after the transformation.

For example:
- Input:
Case 1: N > M
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

Case 2: N < M
4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7

- Output:
Case 1:
6 3 2 6
9 9 9 8
9 6 6 3
7 7 4 9

Case 2:
2 7 4 3
6 2 7 2
7 2 9 1
9 9 0 7
"""

def solve(n, m, a):
    if n == m:
        for i in a:
            print(*i)
    elif n > m:
        cnt = 0
        limit = n - m
        for i in range(n):
            if (i + 1) % 2 == 0 and cnt < limit:
                cnt += 1
                print(*a[i])
            elif cnt >= limit:
                print(*a[i])
    else:
        cnt = 0
        limit = m - n
        mark = [True] * m
        for i in range(n):
            for j in range(m):
                if (j + 1) % 2 == 0 and cnt < limit:
                    mark[j] = False
                    cnt += 1
        for i in range(n):
            for j in range(m):
                if mark[j]:
                    print(a[i][j], end=" ")
            print()

n, m = map(int, input().split())
a = []
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
solve(n, m, a)