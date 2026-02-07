# For example
# 28 = 1 * 2^2 * 7^1
# 100 = 1 * 2^2 * 5^2
# 1234 = 1 * 2^1 * 617^1

def prime_factor(n):
    res = "1"
    
    for i in range(2, int(n**(0.5)) + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        if cnt != 0:
            res += " * " + str(i) + "^" + str(cnt)
        if n == 1:
            return res
    if n != 1:
        res += " * " + str(n) + "^1"
    
    return res

test = int(input())
for _ in range(test):
    n = int(input())
    print(prime_factor(n))