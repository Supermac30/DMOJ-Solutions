"""
    https://dmoj.ca/problem/dwite09c3p5
"""
import sys; input=sys.stdin.readline
import itertools

def checkValid(graph, colouring):
    for node in graph.keys():
        for children in graph[node]:
            if colouring[node-1] == colouring[children-1]:
                return False
    return True
            

for times in range(5):
    graph = {}
    for i in range(int(input())):
        a, b = map(int, input().split())
        if graph.get(a) is None:
            graph[a] = []
        if graph.get(b) is None:
            graph[b] = []
        if a == b:
            continue
        graph[a].append(b)
        graph[b].append(a)
    found = False
    for i in range(1, 5):
        for colouring in itertools.product(list(range(i)), repeat=len(graph.values())):
            if checkValid(graph, colouring):
                found = True
                print(i)
                break
        if found:
            break
    if not found:
        print(0)
