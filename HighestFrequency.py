# Given an array A[] of N elements.
# Your task is to find a number that appears more than N/2 times in the array.
#
# Input:
# - The first line contains the number of test cases T (T <= 10).
# - For each test case:
#   + An integer N (1 <= N <= 100000), the number of elements.
#   + A line containing N integers A[i] (1 <= A[i] <= 1_000_000).
#
# Output:
# - For each test case, print the required number on one line.
# - If multiple numbers satisfy the condition and have the same highest frequency, print the smallest one.
# - If no such number exists, print "NO".

# Using marking array
"""
for test in range(int(input())):
    n = int(input())
    freq = n // 2
    a = list(map(int, input().split()))
    
    check = [0] * (10 ** 6)
    for i in range(n):
        check[a[i]] += 1
        
    res = check.index(max(check))
    print(res if max(check) > freq else "NO")
"""

# Using Boyer - Moore Majority Voting Algorithm (more optimal)
# https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/
for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    votes = 0
    candidate = -1
    # finding majority candidate
    for i in range(n):
        if votes == 0:
            candidate = a[i]
            votes = 1
        else:
            if candidate == a[i]:
                votes += 1
            else:
                votes -= 1
                
    cnt = 0
    # check if the majority candidate appears more then n/2 times
    for i in range(n):
        if candidate == a[i]:
            cnt += 1
    print(candidate if cnt > n // 2 else "NO")