# Given a binary string X[] of length n.
# Your task is to convert this binary string into a number in base b,
# where b can only be one of the following bases: 2, 4, 8, or 16.
#
# Input (text file DATA.in):
# - The first line contains an integer T, the number of test cases.
# - For each test case:
#   + The first line contains b, the base of the number system.
#   + The second line contains the binary string X of length n.
#
# Constraints:
# - 1 ≤ T ≤ 10
# - 1 ≤ n ≤ 10^5
# - X[i] ∈ {0, 1}
#
# Output:
# - Print the result for each test case on a separate line.
#
# For example:
#     Input:
#         2
#         8
#         10010100010010101
#         2
#         10010100010010101
#     Output:
#         224225
#         10010100010010101

display = "0123456789ABCDEF"
f = open("New Text Document.txt")

def convert(n, b):
    if b == 2:
        return bin(n)[2:]
    if b == 8:
        return oct(n)[2:]
    if b == 16:
        return hex(n)[2:].upper()
    res = ""
    while n != 0:
        res += display[n % b]
        n //= b
    return res[::-1]

test = int(f.readline())
for _ in range(test):
    b = int(f.readline().strip())
    n = f.readline().strip()
    dec = int(n, 2)
    print(convert(dec, b))

f.close()

"""NOTE"""
# read(): read the whole file
# readline(): read a single line in the file
# readlines() (with an "s"): read all the lines and put them into a list
# for line in f: traverse through each line