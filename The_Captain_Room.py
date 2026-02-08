# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true

from collections import Counter

k = int(input())
rooms_list = list(map(int, input().split()))
captain_room = Counter(rooms_list) # a dict

for room in captain_room:
    if captain_room[room] == 1: # a separate room
        print(room)