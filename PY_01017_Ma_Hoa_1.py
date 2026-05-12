for _ in range(int(input())):
    s = input()
    res = ""
    cnt = 1
    first = s[0]
    for i in range(1, len(s)):
        if s[i] != first:
            res += str(cnt) + first
            first = s[i]
            cnt = 1
        else:
            cnt += 1
    res += str(cnt) + first
    print(res)