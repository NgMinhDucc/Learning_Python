# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true

n = int(input()) # the number of numbers in set A
A = set(map(int, input().split()))
N = int(input()) # the number of other sets

while N > 0:
    operation = list(input().split())
    
    if operation[0] == "update": # adding elements from other set to the current set
        other_set = set(map(int, input().split()))
        A.update(other_set)
    elif operation[0] == "intersection_update": # keeping elements that are found on both sets
        other_set = set(map(int, input().split()))
        A.intersection_update(other_set)
    elif operation[0] == "difference_update": # removing elements in the current set is they're found in the other
        other_set = set(map(int, input().split()))
        A.difference_update(other_set)
    elif operation[0] == "symmetric_difference_update": # removing elements that are found in both sets
        other_set = set(map(int, input().split()))
        A.symmetric_difference_update(other_set)
    
    N -= 1
        
print(sum(A))