
# Declare a Fraction class with two attributes: numerator and denominator.
# All values are positive integers and have at most 18 digits.
#
# Read two fractions p and q. Compute the sum p + q,
# reduce the result to its simplest form, and print it.
#
# Input:
# - Four positive integers representing the numerator and denominator
#   of fraction p, followed by the numerator and denominator of fraction q.
#
# Output:
# - Print the sum p + q as a simplified fraction, in the same format as shown in the example.
# For exmaple:
# Input:
# 123 456 12 34
# Output:
# 1609/2584

from math import gcd
import sys

def lcm(a, b):
    return a * (b // gcd(a, b))

class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
        
    def calculate_total_then_simplify(self, other):
        total_denominator = lcm(self.den, other.den)
        total_numerator = self.num * (total_denominator // self.den) + other.num * (total_denominator // other.den)

        GCD = gcd(total_numerator, total_denominator)
        total_numerator //= GCD
        total_denominator //= GCD
        return f"{total_numerator}/{total_denominator}"
    
if __name__ == "__main__":
    arr = []
    while len(arr) < 4:
        arr.extend(map(int, sys.stdin.readline().split()))
        
    frac1 = Fraction(arr[0], arr[1])
    frac2 = Fraction(arr[2], arr[3])

    print(frac1.calculate_total_then_simplify(frac2))