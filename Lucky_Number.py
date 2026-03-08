# In Vietnamese culture, a lucky number is a number that contains only the digits 6 and/or 8.
#
# A "beautiful lucky number" is defined as a number that, when read from left to right,
# can be formed by concatenating the numbers: 6, 68, and 688. It is not necessary to use all three of them.
#
# Example:
# 666666, 668688, 688688688 are beautiful lucky numbers.
#
# Given a positive integer N with at most 100 digits, determine whether it is a beautiful lucky number.
#
# Input:
# - A single line containing the integer N (with at most 100 digits).
#
# Output:
# - Print "YES" if N is a beautiful lucky number, otherwise print "NO".
#
# For example:
#     666666 -> YES
#     668668 -> YES
#     886236 -> NO

def luck_num(n):
    cnt = 0
    for i in n:
        if i != "6" and i  != "8":
            return "NO"
        if i == "8":
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return "NO"
    return "YES"

n = input()
print(luck_num(n))