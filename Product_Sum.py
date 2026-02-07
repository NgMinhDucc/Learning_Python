# Given a positive integer N which can be very large (up to 500 digits).
# Consider digit positions from left to right, starting from index 0.
#
# Compute:
# - The product of digits at even positions.
#   (Ignore digits equal to 0 when computing the product; the product value may have up to 18 digits.)
# - The sum of digits at odd positions.
#
# Input:
# - The first line contains the number of test cases (<= 20).
# - Each test case consists of a positive integer N with at least 2 digits and at most 500 digits.
#
# Output:
# - For each test case, print on one line two values: the product of digits at even positions and the sum of digits at odd positions.
#
# Note: If all digits at even positions are 0, print product = 0.

def cal(n):
    total = 0
    product = 1
    no_zero = True
    
    for i in range(len(n)):
        if i % 2 == 1:
            total += int(n[i])
        else:
            if n[i] == "0":
                no_zero = False # to avoid cases like "212121212121"
            elif n[i] != "0" and n[i] != "1":
                product *= int(n[i])
    
    if product == 1 and not no_zero: # only if there is a zero in n, the product will be 0
        product = 0
        
    return product, total

for test in range(int(input())):
    n = input()
    res = cal(n)
    print(res[0], res[1])