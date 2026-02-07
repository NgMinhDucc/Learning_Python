# Given an array A of 10 positive integers.
# Count how many distinct values remain after taking each element modulo 42.
#
# Input:
# - 10 positive integers, given on one or multiple lines.
#
# Output:
# - Print the number of distinct values obtained after applying modulo 42.
# For example: 
# 1. 1 2 3 4 5 6  7 8  9 10
# -> Output: 10 (since there are 10 distinct values remain after taking each element modulo 42).
# 2. 
# 42 84 252 420 840
# 126 42 84 420 126
# -> Output: 1 (since there are 1 distinct values remain after taking each element modulo 42).

"""
# input is put in 1 or various lines
inp = []
while True:
    line = input()
    if line == "":
        break
    inp.append(list(map(int, line.split())))
    
res = []
for li in inp:
    for i in li:
        if i % 42 not in res:
            res.append(i % 42)
print(len(res))

use this code instead of the above one (since this reads the whole input, including 
spaces and \n-s, while the previous one may cause IR)
"""

from sys import stdin

if __name__ == "__main__":
    inp = stdin.read().split()
    numbers = [int(i) for i in inp]
    
    res = set()
    for num in numbers:
        res.add(num % 42)
    print(len(res))