def pal(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

for _ in range(int(input())):
    n = int(input())
    if n % 7 == 0:
        print(n)
    else:
        res = 0
        cnt = 0
        while cnt <= 1000:
            rev = pal(n)
            res = n + rev
            if res % 7 == 0:
                print(res)
                break
            n += rev
            cnt += 1
        if cnt > 1000:
            print(-1)