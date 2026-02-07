# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

# Super complicated code
    # for i in range(1, 2 * size):
    #     if i <= size:
    #         for j in range(2 * i - 1):
    #             if j <= i // 2:
    #                 print(sub_alp[j], end = " ")
    #             else:
    #                 print(sub_alp[2 * (i - 1) - j], end = " ")
    #         print()
    #     else:
    #         scale = 2 * (2 * size - 1 - i) + 1
    #         for j in range(scale):
    #             if j <= scale // 2:
    #                 print(sub_alp[j], end = " ")
    #             else:
    #                 print(sub_alp[scale - j - 1], end = " ")
    #         print()
    
# Cleaner code
    # for i in range(1, 2 * size):
    #     k = i if i <= size else (2 * size - i)
        
    #     for j in range(2 * k - 1):
    #         if j <= k // 2:
    #             print(sub_alp[j], end = " ")
    #         else:
    #             print(sub_alp[2 * (k - 1) - j], end = " ")
    #     print()
    
def print_rangoli(size):
    alp = list(chr(i) for i in range(ord('a'), ord('z') + 1))
    if size == 1:
        print("a")
    else:
        sub_alp = alp[:size]
        sub_alp.reverse()
        
        for i in range(1, 2 * size):
            k = i if i <= size else (2 * size - i)
            s = ""
            scale = 4 * size - 3
            
            for j in range(2 * k - 1):
                if j < k:
                    s += sub_alp[j] + "-"
                else:
                    if (2 * (k - 1) - j) == 0:
                        s += sub_alp[2 * (k - 1) - j]
                    else:
                        s += sub_alp[2 * (k - 1) - j] + "-"
            print(s.center(scale, "-"))
        
# main
n = int(input())
print_rangoli(n)