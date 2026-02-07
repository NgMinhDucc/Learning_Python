# Given 2 positive numbers x1, x2. We're only allowed to change sigits p to digits q and vice versa.
# Return the smallest and biggest sum from x1 and x2, which are created based on the above rules (print the smallest first, then the biggest).
# For example:
# p = 5, q = 6
# x1 = 645, x2 = 666
# Step 1 (change p to q): x1 = 646, x2 = 666 -> sum = 1312
# Step 2 (change q to p): x2 = 545, x2 = 555 -> sum = 1100
# -> Output: 1100, 1312

def cal(a, b, x, y):
    result = int(x.replace(a, b)) + int(y.replace(a, b))
    return result

test = int(input())
for _ in range(test):
    p, q = input().split()
    inp = input().split()
    if len(inp) == 1:
        x1 = inp[0]
        x2 = input()
    else:
        x1, x2 = inp # in case the users input 2 numbers all in 1 line
    
    res1 = cal(p, q, x1, x2)
    res2 = cal(q, p, x1, x2)
    print(min(res1, res2), max(res1, res2))

