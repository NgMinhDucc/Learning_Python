from sys import stdin

inp = stdin.read().split()
a = [int(i) for i in inp]
res = set()
for i in a:
    res.add(i % 42)
print(len(res))