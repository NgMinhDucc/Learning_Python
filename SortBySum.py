# Given an array A consisting of N positive integers, each having at most 6 digits.
#
# Sort the array in increasing order based on the sum of digits of each number.
# If two numbers have the same digit sum, the smaller number should come first.
#
# Input:
# - The first line contains the number of test cases (not more than 10).
# - Each test case consists of 2 lines:
#   + The first line contains an integer N (N < 100).
#   + The second line contains N integers of the array A,
#     all numbers are positive integers and have at most 9 digits.
#
# Output:
# - For each test case, print the sorted array on a single line.

# For example:
# Input:
# 1
# 8
# 143 43 22 99 7 9 1111 10000000

# Output:
# 10000000 22 1111 7 43 143 9 99

def cal(n):
    total = 0
    for i in n:
        total += int(i)
    return total

for test in range(int(input())):
    n = input()
    a = input().split()
    
    a.sort(key = lambda s: (cal(s), len(s), s))
    print(*a)