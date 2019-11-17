"""
  https://dmoj.ca/problem/ccc09j5
"""
import sys;input=sys.stdin.readline
from collections import deque

#thank you solid_pc31
graph={1: [6], 2: [6], 3: [4, 5, 6, 15], 4: [3, 5, 6], 5: [3, 4, 6], 6: [1, 2, 3, 4, 5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10, 12], 10: [9, 11], 11: [10, 12], 12: [9, 11, 13], 13: [12, 14, 15], 14: [13], 15:[3,13], 16:[17,18], 17:[16,18], 18:[16,17]}

def bfs(a, b):
    queue = deque(graph.get(a))
    amount = len(queue)
    counter = 1
    seen = set()
    while queue:
        if amount == 0:
            amount = len(queue)
            counter += 1
        amount-=1
        check = queue.popleft()
        if check == b:
            return counter
        if check in seen:
            continue
        seen.add(check)
        queue.extend(graph.get(check))
    return "Not connected"
    
command = input()[:-1]
while command != "q":
    if command == "i":
        a, b = int(input()), int(input())
        if graph.get(a) is None:
            graph[a] = []
        if graph.get(b) is None:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    elif command == "d":
        a, b = int(input()), int(input())
        graph[a].remove(b)
        graph[b].remove(a)
    elif command == "n":
        print(len(graph.get(int(input()))))
    elif command == "f":
        check = int(input())
        counted = set()
        for friend in graph.get(check):
            for friendOfFriend in graph.get(friend):
                if friendOfFriend not in counted and friendOfFriend not in graph.get(check):
                    counted.add(friendOfFriend)
        print(len(counted)-1)
    elif command == "s":
        print(bfs(int(input()), int(input())))
    command = input()[:-1]
