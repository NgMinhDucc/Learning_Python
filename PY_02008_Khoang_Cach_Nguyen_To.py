from math import sqrt
maxx = 10**6
def sieve(maxx):
    is_prime = [True] * (maxx + 1)
    is_prime[0] = is_prime[1] = False
    limit = int(sqrt(maxx)) + 1
    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i * i, maxx + 1, i):
                is_prime[j] = False
    return is_prime

from sys import stdin
inp = stdin.read().split()
n = int(inp[0])
x = int(inp[1])

primes = sieve(maxx) # boolean
prime = []
for i in range(len(primes)):
    if primes[i]:
        prime.append(i)
        
idx = 0
while n + 1:
    print(x, end=" ")
    x += prime[idx]
    idx += 1
    n -= 1