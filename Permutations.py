# Given a string S of at most 9 uppercase letters, with no spaces.
# All characters in S are distinct and already sorted from left to right in lexicographical order.
#
# List all permutations of string S in lexicographical order, printing each permutation on a separate line.
#
# Input:
# - A single line containing string S (length <= 9).
#
# Output:
# - Print all permutations in lexicographical order, one permutation per line.
#
# Note:
# - The first permutation is the original string S.

from itertools import permutations

s = input()

li = []
for ch in s:
    li.append(ch)
        
res = permutations(li)
for per in res:
    for p in per:
        print(p, end = "")
    print()