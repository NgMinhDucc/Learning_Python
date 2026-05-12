n = int(input())
a = list(map(int, input().split()))
k = 2
res = [0] * k
fin = []

def Try(i, pos):
    for j in range(pos, n - k + i + 1):
        res[i] = a[j]
        if i == k - 1:
            if res[0] > res[1]:
                fin.append(res)
        else:
            Try(i + 1, j + 1)

Try(0, 0)
print(len(fin))