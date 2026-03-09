# Given a numeric string with length not exceeding 1000 and containing no digit '0'.
#
# Starting from the left, take digits two at a time to form numbers.
# If the final step does not have enough digits to form a two-digit number, the remaining digit is ignored.
#
# This process produces an array A[] consisting only of two-digit integers.
#
# Given an additional positive integer K, called the minimum threshold.
# List the numbers that appear at least K times in A[], in increasing order.
#
# Input:
# - The first line contains the numeric string (length ≤ 1000).
# - The input is guaranteed not to contain the digit '0'.
# - The second line contains the positive integer K (K ≤ 100).
#
# Output:
# - Print the distinct numbers in A[] that appear at least K times, along with their corresponding frequencies.
# - Each result is printed on a separate line in increasing order.
# - If no such number exists, print "NOT FOUND".
#
# For example:
# 124356141111434356149
# 2
# ->  11 2
#     14 2
#     43 3
#     56 2
#
# 124356141111434356149
# 10
# -> NOT FOUND

s = input()
k = int(input())
a = {}
while len(s) > 0:
    x = int(s[:2])
    if len(str(x)) == 2:
        if a.get(x) is None:
            a[x] = 1
        else:
            a[x] += 1
    s = s[2:]
    
new = dict(sorted(a.items()))
mark = 0
for i in new:
    if new[i] >= k:
        mark = 1
        print(i, new[i])
        
if mark == 0:
    print("NOT FOUND")