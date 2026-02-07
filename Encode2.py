# Given a standard character set P of 28 characters:
# 26 uppercase letters from 'A' to 'Z', followed by '_' and '.'
# P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
#
# An encryption with shift K (0 < K < 28) replaces each character s[i]
# by the character at position (i + K) % 28 in P.
#
# Example: with K = 3, 'A' -> 'D', 'B' -> 'E', '.' -> 'C'.
#
# Given an integer K and a string S (containing only characters from P,
# with no spaces), encrypt S using the rule above,
# then reverse the encrypted string.

P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
#    0123456789012345678901234567
ip = 1
while ip != 0:
    ip = input().split()
    
    if ip[0] == "0": # only stop when k = "0"
        break
    else:
        k = int(ip[0])
        s = ip[1]
        res = ""
        
        for ch in s:
            res += P[(P.index(ch) + k) % 28]
        print(res[::-1])
        
