# Given a positive integer N with at most 9 digits.
# Round N according to the following rules:
#
# - If N > 10, round it to the nearest ten.
# - If the result is greater than 100, round it to the nearest hundred.
# - If the result is greater than 1000, round it to the nearest thousand.
# - Continue in this manner for higher powers of 10.
#
# Note: A digit 5 is always rounded up.

for _ in range(int(input())):
    li = list(int(i) for i in input())
    
    for i in range(len(li) - 1, 0, -1):
        if li[i] >= 5:
            li[i - 1] += 1
        li[i] = 0
        
    if li[0] == 10:
        li[0] = 0
        li = [1] + li
        
    for i in li:
        print(i, end = "")
    print()