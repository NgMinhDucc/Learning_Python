# Given a string S[] consisting only of digits, with length not exceeding 1000, and a positive integer N (with at most 9 digits).
# Count how many times the number N appears in the string S[].
#
# Note: Digits must not be counted more than once. That is, each character position in the string can be used only once.
#
# Example:
# S[] = "1212121112211221121", N = 121
# The answer is 3.
#
# Input:
# - The first line contains the number of test cases (not more than 20).
# - Each test case consists of two lines:
#   + The first line is the string S[].
#   + The second line is the number N.
#
# Output: For each test case, print the computed result on a separate line.
# For example:
#     Input:
#         2
#         1212121112211221121
#         121
#         2222222222322292
#         2222
#     Output:
#         3
#         2

test = int(input())
for _ in range(test):
    s = input()
    n = input()
    idx = s.find(n) # return the first occurence of n in s
    cnt = 0
    while idx != -1:
        cnt += 1
        idx = s.find(n, idx + len(n))
    print(cnt)