# Given a positive integer N.
# If N is divided by 7 -> return N.
# Else -> At each step, calculate sum of N with its palindrome, stop when the sum is divided by 7 or the step pasts 1000 (return -1 at this case).

def rev(n):
    r = 0
    while n != 0:
        r = r * 10 + n % 10
        n //= 10
    return r

# main
test = int(input())
for _ in range(test):
    n = input()
    if int(n) % 7 == 0:
        print(n)
    else:
        count = 0
        flag = True
        sum = int(n)
        while sum % 7 != 0:
            sum += rev(sum)
            count += 1
            if count > 1000:
                flag = False
                print(-1)
                break
        if flag == True:
            print(sum)

