# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=truem = int(input())

a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

sym_diff = a.symmetric_difference(b)
sorted_sym_diff = sorted(sym_diff)
for i in sorted_sym_diff:
    print(i)