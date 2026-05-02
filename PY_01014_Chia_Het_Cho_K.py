a, k, n = map(int, input().split())
start = (a // k + 1) * k # lowest k's multiple that bigger than a
if start >= n:
    print(-1)
else:
    for i in range(start, n + 1, k):
        print(i - a, end=" ")