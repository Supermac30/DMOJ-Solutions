"""
  https://dmoj.ca/problem/ccc10s4
"""
import sys; input=sys.stdin.readline
N = int(input())
graph = []
pens = []
for i in range(N):
    graph.append({})
    pens.append({})
    info = list(map(int, input().split()))
    size = info[0]
    for j in range(1, size):
        graph[i][tuple(sorted((info[j], info[j+1])))] = info[j+size]
    graph[i][tuple(sorted((info[size], info[1])))] = info[2*size]

pens.append({})

for i in range(N):
    for edge in graph[i].keys():
        found = False
        for j in range(i+1, N):
            if edge in graph[j]:
                found = True
                other = float('inf')
                if i in pens[j]:
                    other = pens[j].get(i)
                pens[i][j] = min(other, graph[j].get(edge))
                pens[j][i] = min(other, graph[j].get(edge))
                del graph[j][edge]
                break
        if not found:
            other = float('inf')
            if i in pens[N]:
                other = pens[N].get(i)
            pens[i][N] = min(other, graph[i].get(edge))
            pens[N][i] = min(other, graph[i].get(edge))

pensCopy = []
for i in range(N+1):
    pensCopy.append(pens[i].copy())
    if N in pens[i]:
        del pens[i][N]
del pens[-1]

def beginning(graph):
    minimum = [float('inf'), 0, 0] # Weight, start, end
    for i in range(len(graph)):
        for dest in graph[i].keys():
            if minimum[0] > pens[i].get(dest):
                minimum = [pens[i].get(dest), i, dest]
    return minimum

minimum = beginning(pens)
verticies = [minimum[1], minimum[2]]
cost0 = minimum[0]
del pens[minimum[1]][minimum[2]]
del pens[minimum[2]][minimum[1]]
while len(verticies) != N:
    minimum = [float('inf'), 0, 0] # Weight, start, end
    for check in verticies:
        for dest in pens[check].keys():
            if dest in verticies:
                continue
            if minimum[0] > pens[check].get(dest):
                minimum = [pens[check].get(dest), check, dest]
    if minimum[0] == float('inf'):
        cost0 = float('inf')
        break
    else:
        cost0 += minimum[0]
        del pens[minimum[2]][minimum[1]]
        del pens[minimum[1]][minimum[2]]
        verticies.append(minimum[2])


pens = pensCopy

minimum = beginning(pens)
verticies = [minimum[1], minimum[2]]
cost1 = minimum[0]
del pens[minimum[1]][minimum[2]]
del pens[minimum[2]][minimum[1]]
while len(verticies) != N+1:
    minimum = [float('inf'), 0, 0] # Weight, start, end
    for check in verticies:
        for dest in pens[check].keys():
            if dest in verticies:
                continue
            if minimum[0] > pens[check].get(dest):
                minimum = [pens[check].get(dest), check, dest]
    if minimum[0] == float('inf'):
        minimum = beginning(pens)
        cost1 += minimum[0]
        del pens[minimum[1]][minimum[2]]
        del pens[minimum[2]][minimum[1]]
        verticies.extend([minimum[1], minimum[2]])
    else:
        cost1 += minimum[0]
        del pens[minimum[1]][minimum[2]]
        del pens[minimum[2]][minimum[1]]
        verticies.append(minimum[2])
print(min(cost0, cost1))
