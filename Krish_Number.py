# A positive integer N is called a Krish number if the sum of the factorials
# of its digits is equal to the number itself.
# Example: N = 145 is a Krish number because 1! + 4! + 5! = 145.
#
# Given a positive integer N, determine whether it is a Krish number.
# Print "Yes" if N is a Krish number, otherwise print "No".
#
# Input:
# - The first line contains an integer T, the number of test cases.
# - The next T lines each contain one positive integer N.
# - Constraints: 1 ≤ T ≤ 100, 1 ≤ N ≤ 10^8.
#
# Output:
# - For each test case, print the result on a separate line.
# For example:
# Input:
# 2
# 145
# 235
# Ouput:
# Yes
# No

f = [1] * 10
def factor():
    for i in range(1, 10):
        f[i] = i * f[i - 1]
    return f

def solve(n):
    fact = factor()
    tong = 0
    for i in n:
        tong += fact[int(i)]
    return  "Yes" if tong == int(n) else "No"
        

for test in range(int(input())):
    n = input()
    print(solve(n))