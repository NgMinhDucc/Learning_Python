def check(n):
    if len(n) < 3:
        return False
    else:
        idx = n.index(max(n))
        n1 = n[:idx] # first half, should be strictly increased
        n2 = n[idx:] # second half, should be strictly decreased
        
        for i in range(1, len(n1)):
            if n1[i] <= n1[i - 1]:
                return False
        for i in range(1, len(n2)):
            if n2[i] >= n2[i - 1]:
                return False
        return True

for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")