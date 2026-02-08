# A positive integer is called "prime-dominant" if it satisfies both conditions:
# 1. The number of its digits is a prime number.
# 2. The count of prime digits is greater than the count of non-prime digits.
#
# Write a program to check whether a given positive integer satisfies
# the prime-dominant property.
#
# Input:
# - The first line contains the number of test cases (<= 20).
# - Each test case contains a positive integer N with at least 3 digits
#   and at most 500 digits.
#
# Output:
# - For each test case, print "YES" if N is prime-dominant, otherwise print "NO".

def sieve(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if p[i]:
            for j in range(i * i, n + 1, i):
                p[j] = False
                
    prime = []
    for i in range(len(p)):
        if p[i]:
            prime.append(i)
    return prime

for test in range(int(input())):
    n = input()
    is_prime = sieve(len(n))
    
    cnt = 0
    # number of prime digits in n
    for i in n:
        if int(i) in is_prime:
            cnt += 1
            
    print("NO" if len(n) not in is_prime or cnt <= len(n) - cnt else "YES")