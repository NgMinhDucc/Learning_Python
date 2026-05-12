n, k = map(int, input().split())
a = set(map(int, input().split()))
a = sorted(list(a))
res = [0] * k

def Try(i, pos):
    for j in range(pos, len(a) - k + i + 1):
        res[i] = a[j]
        if i == k - 1:
            for x in res:
                print(x, end=" ")
            print()
        else:
            Try(i + 1, j + 1)
Try(0, 0)