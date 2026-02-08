# Given an array A consisting of N elements.
# For each position i in the array, determine the length of the longest
# contiguous segment ending at position i and extending backward,
# such that all values in that segment are less than or equal to A[i].
#
# Input:
# - The first line contains the number of test cases (not more than 10).
# - Each test case consists of 2 lines:
#   + The first line contains an integer N (1 ≤ N ≤ 10^5).
#   + The second line contains N integers A1, A2, ..., AN (1 ≤ Ai ≤ 10^6).
#
# Output:
# - For each test case, print the resulting array on a single line.
# For example:
# Input:
# 1
# 7
# 100 80 60 70 60 75 85
# Output:
# 1 1 1 2 1 4 6

for test in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    span = [0] * n
    st = []
    for i in range(n):
        while len(st) != 0 and arr[i] >= arr[st[-1]]:
            st.pop()
        if len(st) == 0:
            span[i] = i + 1
        else:
            span[i] = i - st[-1]
        st.append(i)
    print(*span)