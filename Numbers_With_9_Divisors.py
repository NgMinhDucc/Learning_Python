# Given a positive integer N.
# Count how many positive integers less than or equal to N have exactly 9 divisors.
#
# Input:
# - A single line containing an integer N (1 ≤ N ≤ 10^9).
#
# Output:
# - Print the number of integers that have exactly 9 divisors.

def count_numbers_with_9_divisors(n):
    count = 0
    limit = int(n**0.5) + 1
    # To optimize memory, only calculate to n**0.5
    p = [True] * (limit + 1)
    for i in range(2, int(limit**0.5) + 1):
        if p[i]:
            for j in range(i * i, limit + 1, i):
                p[j] = False
    is_prime = [i for i in range(2, limit + 1) if p[i]]
    # p^8
    count += sum(1 for p in is_prime if p**8 <= n)
    # p^2 * q^2
    for i in range(len(is_prime)):
        for j in range(i + 1, len(is_prime)):
            if is_prime[i]**2 * is_prime[j]**2 <= n:
                count += 1
            else:
                break
    return count

n = int(input())
print(count_numbers_with_9_divisors(n))