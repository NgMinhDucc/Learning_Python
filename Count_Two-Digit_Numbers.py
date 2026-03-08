# Given a numeric string with length not exceeding 1000 and containing no digit '0'.
#
# Starting from the left, take digits two at a time to form numbers.
# If the last step does not have enough digits to form a two-digit number, that remaining digit is ignored.
#
# This process produces an array A[] consisting only of two-digit integers.
#
# List and count the distinct numbers that appear in A[], in the order of their first appearance.
#
# Input:
# - A single line containing the numeric string (length ≤ 1000).
# - The input is guaranteed not to contain the digit '0'.
#
# Output:
# - For each distinct number in A[], print the number and its frequency, in the order of appearance. 
# Each pair should be printed on a separate line.
#
# For example:
#     124356141111434356149
#     -> 12 1
#        43 3
#        56 2
#        14 2
#        11 2

s = input()
a = {} # a dictionary
while len(s) > 0:
    x = s[:2]
    if len(x) == 2:
        if a.get(x) is None: # the number does not exist in the dict yet
            a[x] = 1
        else: #otherwise
            a[x] += 1
    s = s[2:]
for i in a:
    print(i, a[i])