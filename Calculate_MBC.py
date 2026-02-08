# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

from math import sqrt, acos, degrees
# acos returns the cosine value of a number (arccos)
# degrees to convert the radian value from acos to degree

ab = int(input())
bc = int(input())

ac = sqrt(ab ** 2 + bc ** 2)
mb = ac / 2
mbc = degrees(acos(bc / (2 * mb)))

mbc += 0.5
print(f"{int(mbc)}{chr(176)}") # chr(176) = °