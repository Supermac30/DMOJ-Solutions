"""
  https://dmoj.ca/problem/gfssoc1j5
"""
import sys; input=sys.stdin.readline
from collections import deque
N, M, T = map(int, input().split())
hallways = {}
for i in range(1, N+1):
    hallways[i] = []
for i in range(M):
    a, b = map(int, input().split())
    hallways[a].append(b)

def bfs(a):
    queue = deque(hallways[a])
    amount = len(queue)
    counter = 1
    seen = set()
    distances = [-1]*N
    while queue:
        if amount == 0:
            amount = len(queue)
            counter += 1
        check = queue.popleft()
        amount -= 1
        if check in seen:
            continue
        seen.add(check)
        distances[check-1] = counter
        queue.extend(hallways[check])
    return distances
        
memory = []
for i in range(1, N+1):
    memory.append(bfs(i))
for i in range(int(input())):
    a, b = map(int, input().split())
    if memory[a-1][b-1] == -1:
        print("Not enough hallways!")
    else:
        print(memory[a-1][b-1]*T)
