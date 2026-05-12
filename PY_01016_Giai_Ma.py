for i in range(int(input())):
    s = input()
    res = ""
    for i in range(0, len(s), 2):
        l = s[i]
        n = int(s[i + 1])
        res += l * n
    print(res)