# Given a string of letters (may have both uppercase and lowercase) and digits.
# Encode the string by writing the number of a character before it.
# For example:
# AACDDPQ -> 2A1C2D1P1Q (since we have 2 'A', 1 'C', 2 'D', 1 'P', and 1 'Q')
# 11111147g -> 6114171g (since we have 6 '1', 1 '4', 1 '7', and 1 'g')

test = int(input())
for _ in range(test):
    s = input()
    l, r = 0, 0
    result = ""
    
    while l < len(s):
        while r < len(s) and s[l] == s[r]:
            r += 1
        count = r - l
        result += str(count) + s[l]
        l = r
    
    print(result)