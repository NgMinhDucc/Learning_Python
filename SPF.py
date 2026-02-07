# Smallest Prime Factor

def sieve_spf(n):
    p = list(range(n + 1))
    p[0] = p[1] = 0
    limit = int(n * 0.5) + 1
    for i in range(2, limit):
        if p[i] == i:
            for j in range(i * i, n + 1, i):
                if p[j] == j:
                    p[j] = i
    return p

print(sieve_spf(100))