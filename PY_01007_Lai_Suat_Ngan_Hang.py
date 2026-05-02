for _ in range(int(input())):
    inp = input().split()
    n = float(inp[0])
    x = float(inp[1])
    m = float(inp[2])
    cnt = 0
    while n <= m:
        n += n * x // 100
        cnt += 1
    
    print(cnt)