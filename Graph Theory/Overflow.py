"""
  https://dmoj.ca/problem/hci16oversleep
"""
import sys; input=sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
start = (0,0)
end = (0,0)
graph = []
for i in range(n):
    line = input()[:-1]
    if 's' in line:
        start = (i, line.index('s'))
    if 'e' in line:
        end = (i, line.index('e'))
    graph.append(line)

def children(loc):
    answer = []
    x, y = loc
    if x-1 >= 0 and graph[x-1][y] != "X":
        answer.append((x-1, y))
    if y-1 >= 0 and graph[x][y-1] != "X":
        answer.append((x, y-1))
    if x+1 < n and graph[x+1][y] != "X":
        answer.append((x+1, y))
    if y+1 < m and graph[x][y+1] != "X":
        answer.append((x, y+1))
    return answer

queue = deque(children(start))
counter = 0
amount = len(queue)
seen = set()
found = False
while queue:
    if amount == 0:
        counter += 1
        amount = len(queue)
    amount -= 1
    check = queue.popleft()
    if check in seen:
        continue
    seen.add(check)
    if check == end:
        print(counter)
        found = True
        break
    queue.extend(children(check))
if not found:
    print(-1)
