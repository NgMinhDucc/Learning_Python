# Declare a Rectangle class with 3 attributes:
# - Length: integer
# - Width: integer
# - Color: string
#
# Read the values of the two sides of the rectangle and its color.
# Print the information about the rectangle including: perimeter, area, and color (formatted in standard form where
# the first letter is uppercase and the remaining letters are lowercase).
#
# Input:
# - Two integers representing the lengths of the rectangle sides, and one string (without spaces) representing the color.
#
# Output:
# - If the rectangle is valid (both sides are positive integers), print 3 values: perimeter, area, and color, separated by a space.
# - If the input data is invalid, print "INVALID".
# This task required the following main function:
# For example:
# Input:
# 10 2 RED
# Output:
# 24 20 Red
"""
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
"""

class Rectangle:
    def __init__(self, length, width, colour):
        if length <= 0 or width <= 0 or length <= width:
            print("INVALID")
            exit()
        
        self.length = length
        self.width = width
        self.colour = colour
        
    def perimeter(self):
        return ((self.length + self.width) * 2)
    
    def area(self):
        return (self.length * self.width)
    
    def color(self):
        self.colour = self.colour.lower()
        self.colour = self.colour[0].upper() + self.colour[1:]
        return self.colour

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))