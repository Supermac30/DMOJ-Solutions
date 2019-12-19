"""
  https://dmoj.ca/problem/vmss15c1p4
"""
import sys, heapq;input=sys.stdin.readline
T, N, M, G = map(int, input().split())
basics = []
for i in range(G):
    basics.append(int(input()))
roads = {}
seen = set()
for i in range(M):
    A, B, L = map(int, input().split())
    if A not in roads:
        roads[A] = []
    if B not in roads:
        roads[B] = []
    seen.add(A)
    seen.add(B)
    roads.get(A).append((B, L))

#finds the minimum paths
costs = [0]+[float("inf")]*(M)
at = 0
while seen:
    minimum = [next(iter(seen)), float("inf")]
    for num in seen:
        if costs[num] < minimum[1]:
            minimum = [num, costs[num]]
    at = minimum[0]
    for path in roads.get(at):
        if costs[at]+path[1] < costs[path[0]]:
            costs[path[0]] = costs[at]+path[1]
    seen.remove(at)

counter=0
for basic in basics:
    if costs[basic] < T:
        counter+=1
print(counter)
