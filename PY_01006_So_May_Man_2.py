for _ in range(int(input())):
    s = input()
    flag = 1
    for i in s:
        if i != "4" and i != "7":
            flag = 0
            break
    
    print("YES" if flag == 1 else "NO")