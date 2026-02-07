# Algorithm: https://www.geeksforgeeks.org/dsa/c-program-for-tower-of-hanoi/
# # Game: https://www.mathsisfun.com/games/towerofhanoi.html

def Hanoi_Tower(n, a, b, c):
    if n == 1:
        print(a, "->", c)
        return
    else:
        Hanoi_Tower(n - 1, a, c, b)
        print(a, "->", c)
        Hanoi_Tower(n - 1, b, a, c)

n = int(input())
Hanoi_Tower(n, "A", "B", "C")