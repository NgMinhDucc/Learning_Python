# Calculate perimater and area of a triangle

from math import sqrt

class Point:
    def __init__(self, coor_x, coor_y):
        self.x = coor_x
        self.y = coor_y
    
    def distance(self, other):
        return sqrt(pow((other.x - self.x), 2) + pow((other.y - self.y), 2)) # distance between 2 points = side's length
        
def solve(p1, p2, p3):
    AB = p1.distance(p2)
    AC = p1.distance(p3)
    BC = p2.distance(p3)
    
    if AB + AC <= BC or AB + BC <= AC or AC + BC <= AB:
        return "INVALID"
    else:
        # P = AB + AC + BC
        # return "{:.3f}".format(P)
        S = sqrt((AB + AC + BC) * (AB + AC - BC) * (AC + BC - AB) * (AB + BC - AC)) / 4 # Heron formula
        return "{:.2f}".format(S)
        
def Decimal(coordinate):
    return float(coordinate)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        p3 = Point(Decimal(arr[4]), Decimal(arr[5]))
        print(solve(p1, p2, p3))
        t -= 1