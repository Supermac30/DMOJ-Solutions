"""
  https://dmoj.ca/problem/dmopc13c3p3
"""
import sys; input=sys.stdin.readline
from collections import deque
N, H = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input()[:-1].split())))

def children(loc):
    poss = []
    if loc[0] - 1 >= 0 and abs(field[loc[0]][loc[1]] - field[loc[0]-1][loc[1]]) <= H:
        poss.append((loc[0]-1, loc[1]))
    if loc[0] + 1 < N and abs(field[loc[0]][loc[1]] - field[loc[0]+1][loc[1]]) <= H:
        poss.append((loc[0]+1, loc[1]))
    if loc[1] - 1 >= 0 and abs(field[loc[0]][loc[1]] - field[loc[0]][loc[1]-1]) <= H:
        poss.append((loc[0], loc[1]-1))
    if loc[1] + 1 < N and abs(field[loc[0]][loc[1]] - field[loc[0]][loc[1]+1]) <= H:
        poss.append((loc[0], loc[1]+1))
    return poss

queue = deque(children((0, 0)))
amount = len(queue)
counter = 1
seen = set()
found = False
while queue:
    if amount == 0:
        amount = len(queue)
        counter +=1
    amount -= 1
    check = queue.popleft()
    if check == (N-1, N-1):
        found = True
        break
    if check in seen:
        continue
    seen.add(check)
    queue.extend(children(check))
print("yes" if found else "no")
