# Declare a Point class (a point in 2D space) with two attributes: x-coordinate and y-coordinate (both are real numbers).
# Read two points p1 and p2, then compute the distance between them.
#
# Input:
# - The first line contains the number of test cases (not more than 20).
# - Each test case consists of 4 real numbers representing the coordinates of two points A and B (|value| ≤ 1000).
#
# Output:
# - For each test case, print the distance between the two points rounded to 4 decimal places.
# For example:
# Input:
# 2
# 0 0 0 5
# 0 199 5 6
# Output:
# 5.0000
# 193.0648
#
# This task requires the following main function:
"""
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1
"""

from math import sqrt

class Point:
    def __init__(self, coor_x, coor_y):
        self.x = coor_x
        self.y = coor_y
        
    def distance(self, other):
        # access coordinate via attribute since "other" is an object
        d = sqrt(pow(other.x - self.x, 2) + pow(other.y - self.y, 2)) # Euclidean distance
        return "{:.4f}".format(d)

def Decimal(coordinate):
    return float(coordinate)
                
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1