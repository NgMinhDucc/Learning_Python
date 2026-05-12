P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = input().split()
    if inp[0] == "0":
        break
    else:
        k = int(inp[0])
        s = inp[1]
        res = ""
        for i in s:
            res += P[(P.index(i) + k) % 28]
        print(res[::-1])