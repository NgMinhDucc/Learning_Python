# Given a binary number, a simple rule can be used to convert it to base 8 (octal):
# Starting from the rightmost side of the binary number, group the bits into
# consecutive groups of three digits. Then convert each group into its
# corresponding decimal value; the sequence of these values forms the octal representation of the number.
#
# If the leftmost (final) group has fewer than three bits, pad it with leading zeros to make it three bits long.
#
# Apply this rule to convert a binary number (with at most 100 bits and always starting with digit '1') into its base-8 representation.
#
# Input:
# - A single binary number, with length not exceeding 100 digits.
#
# Output:
# - Print the corresponding number in base 8.
# For example:
#     Input:
#         1010
#         11001100
#     Output:
#         12
#         314

import sys

def convert_to_octal(n):
    bi = ""
    res = ""
    for i in range(len(n) - 1, -1, -1):
        bi += n[i]
        if len(bi) == 3:
            bi = bi[::-1]
            de = int(bi[0]) * 4 + int(bi[1]) * 2 + int(bi[2])
            res += str(de)
            bi = ""
    
    if len(bi) != 0:
        bi = bi[::-1] 
        while len(bi) < 3:
            bi = "0" + bi
        de = int(bi[0]) * 4 + int(bi[1]) * 2 + int(bi[2])
        res += str(de)
    return res[::-1]

if __name__ == "__main__":
    n = sys.stdin.readline().strip() # a binary
    print(convert_to_octal(n))