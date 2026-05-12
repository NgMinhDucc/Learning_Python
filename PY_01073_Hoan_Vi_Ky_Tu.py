s = input()
n = len(s)
used = [False] * n
res = [""] * n

def Try(i):
    for j in range(n):
        if used[j] == False:
            res[i] = s[j]
            used[j] = True
            if i == n - 1:
                for x in res:
                    print(x, end="")
                print()
            else:
                Try(i + 1)
            used[j] = False
            
Try(0)