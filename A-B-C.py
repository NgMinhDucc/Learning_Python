# List all strings whose length does not exceed N, formed only from the characters A, B, C, and satisfying the following conditions:
# - The string contains all three characters A, B, and C.
# - The number of character A is not greater than the number of character B.
# - The number of character B is not greater than the number of character C.

# Input: A single line containing an integer N (N ≤ 12).

# Output:
# - Print all valid strings in order of increasing length.
# - If multiple strings have the same length, print them in lexicographical (dictionary) order.
# - Print each string on a separate line.

# For example: 
# n = 4
# -> Output:
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA
# ABCC
# ACBC
# ACCB
# BACC
# BCAC
# BCCA
# CABC
# CACB
# CBAC
# CBCA
# CCAB
# CCBA

def Try(s, n, num_a, num_b, num_c):
    # still generate all the results, then check one by one
    if len(s) == n and num_a > 0 and num_a <= num_b and num_b <= num_c:
        print(s)
    if len(s) < n:
        Try(s + "A", n, num_a + 1, num_b, num_c)
        Try(s + "B", n, num_a, num_b + 1, num_c)
        Try(s + "C", n, num_a, num_b, num_c + 1)

n = int(input())
for i in range(3, n + 1):
    Try("", i, 0, 0, 0)