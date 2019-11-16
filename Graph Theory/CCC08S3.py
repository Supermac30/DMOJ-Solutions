"""
  https://dmoj.ca/problem/ccc08s3
"""
import sys; input=sys.stdin.readline
from collections import deque
def children(loc, city):
    place = city[loc[0]][loc[1]]
    poss = []
    if place == "|" or place == "+":
        if loc[0] - 1 >= 0 and city[loc[0]-1][loc[1]] != "*":
            poss.append((loc[0]-1, loc[1]))
        if loc[0] + 1 < len(city) and city[loc[0]+1][loc[1]] != "*":
            poss.append((loc[0]+1, loc[1]))
    if place == "-" or place == "+":
        if loc[1] - 1 >= 0 and city[loc[0]][loc[1]-1] != "*":
            poss.append((loc[0], loc[1]-1))
        if loc[1] + 1 < len(city[0]) and city[loc[0]][loc[1]+1] != "*":
            poss.append((loc[0], loc[1]+1))
    return poss

for i in range(int(input())):
    R = int(input())
    C = int(input())
    city = []
    for i in range(R):
        city.append(list(input()[:-1]))
    queue = deque(children((0,0), city))
    amount = len(queue)
    if len(city) == 1 and len(city[0]) == 1:
        print(1)
        continue
    counter = 2
    seen = set()
    found = False
    while queue:
        if amount == 0:
            amount = len(queue)
            counter += 1
        amount -= 1
        check = queue.popleft()
        if check == (R-1, C-1):
            print(counter)
            found = True
            break
        if check in seen:
            continue
        seen.add(check)
        queue.extend(children(check, city))
    if not found:
        print(-1)
