# Given three arrays A[], B[], and C[], each sorted in non-decreasing order, with sizes N, M, and K respectively.
# Your task is to find the elements that are common to all three arrays.
#
# Input:
# - The first line contains an integer T, the number of test cases (T ≤ 20).
# - Each test case starts with three integers N, M, and K (1 ≤ N, M, K ≤ 100000).
# - The next line contains N integers A[i], followed by M integers B[i], and K integers C[i].
# - (0 ≤ A[i], B[i], C[i] ≤ 10^9)
#
# Output:
# - For each test case, print the result on a single line.
# - If no common element exists, print "NO".
# For example:
#     Input:
#         3
#         6 5 8
#         1 5 10 20 40 80
#         5 7 20 80 100
#         3 4 15 20 30 70 80 120
#         3 5 4
#         1 5 5
#         3 4 5 5 10
#         5 5 10 20
#         3 3 3
#         1 2 3
#         4 5 6
#         7 8 9
#     Output:
#         20 80
#         5 5
#         NO

def Intersection(n, m, k, a, b, c):
    x, y, z = 0, 0, 0
    res = []
    while x < n and y < m and z < k:
        if a[x] == b[y] and b[y] == c[z]:
            res.append(a[x])
            x += 1
            y += 1
            z += 1
        else:
            MIN = min({a[x], b[y], c[z]})
            if a[x] == MIN:
                x += 1
            if b[y] == MIN:
                y += 1
            if c[z] == MIN:
                z += 1
    
    if len(res) == 0:
        print("NO")
    else:
        print(*res)

test = int(input())
for _ in range(test):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    Intersection(n, m, k, a, b, c)