# Given an array A[] of N ppositive integers (1<N<10^5, 1<=A[i]<=100).
# While there exists a pair of adjacent elements whose sum is even, remove that pair from the array and shift the remaining
# elements to form a continguos array.
# Repeat the process until no such pair exists.
# Return the final size of the array.

n = int(input())
li = list(map(int, input().split()))
stack = []
stack.append(li[0])
for i in range(1, n):
    if len(stack) != 0 and (li[i] + stack[-1]) % 2 == 0:
        stack.pop()
    else:
        stack.append(li[i])
print(len(stack))