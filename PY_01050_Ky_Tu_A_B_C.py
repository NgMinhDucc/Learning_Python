def Try(s, n, numa, numb, numc):
    if len(s) == n and numa > 0 and numa <= numb and numb <= numc:
        print(s)
    if len(s) < n:
        Try(s + "A", n, numa + 1, numb, numc)
        Try(s + "B", n, numa, numb + 1, numc)
        Try(s + "C", n, numa, numb, numc + 1)

n = int(input())
for i in range(3, n + 1):
    Try("", i, 0, 0, 0)