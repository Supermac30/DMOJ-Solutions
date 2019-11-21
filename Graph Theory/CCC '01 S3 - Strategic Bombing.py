"""
  https://dmoj.ca/problem/ccc01s3
"""
import sys; input=sys.stdin.readline
from collections import deque
graph = {}
inp = input()
while inp != "**\n":
    if inp[0] not in graph:
        graph[inp[0]] = []
    if inp[1] not in graph:
        graph[inp[1]] = []
    graph[inp[0]].append(inp[1])
    graph[inp[1]].append(inp[0])
    inp = input()

def bfs():
    queue = deque(graph["A"])
    seen = set()
    while queue:
        check = queue.popleft()
        if check in seen:
            continue
        seen.add(check)
        if check == "B":
            return False
        queue.extend(graph[check])
    return True

seen = set()
counter = 0
for city in graph.keys():
    for connected in graph[city]:
        if city+connected in seen or connected+city in seen:
            continue
        seen.add(city+connected)
        graph[city].remove(connected)
        graph[connected].remove(city)
        if bfs():
            counter += 1
            print(city+connected)
        graph[city].append(connected)
        graph[connected].append(city)
print("There are {} disconnecting roads.".format(counter))
