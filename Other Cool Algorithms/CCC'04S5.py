"""
  https://dmoj.ca/problem/ccc04j5
"""
L, W, X = map(int, input().split())
lines = [((0, 1), (W, 1))]
for i in range(L):
    temp = []
    for line in lines:
        if line[0][0] == line[1][0]:
            dist = (line[1][1]-line[0][1])//3
            temp.extend([(line[0], (line[0][0], line[0][1]+dist)), ((line[0][0], line[0][1]+dist), (line[0][0]-dist, line[0][1]+dist)), \
                         ((line[0][0]-dist, line[0][1]+dist), (line[0][0]-dist, line[0][1]+2*dist)), \
                         ((line[0][0]-dist, line[0][1]+2*dist), (line[0][0], line[0][1]+2*dist)), ((line[0][0], line[0][1]+2*dist), line[1])])
        else:
            dist = (line[1][0]-line[0][0])//3
            temp.extend([(line[0], (line[0][0]+dist, line[0][1])), ((line[0][0]+dist, line[0][1]), (line[0][0]+dist, line[0][1]+dist)), \
                         ((line[0][0]+dist, line[0][1]+dist), (line[0][0]+2*dist, line[0][1]+dist)), ((line[0][0]+2*dist, line[0][1]+dist), (line[0][0]+2*dist, line[0][1])), \
                         ((line[0][0]+2*dist, line[0][1]), line[1])])
            
    lines = temp[::]
inside = []
for line in lines:
    if line[0][0] == line[1][0]:
        if line[0][0] == X:
            inside.extend(list(range(line[0][1], line[1][1]+1)))
    else:
        if line[0][0] <= X and line[1][0] >= X or line[0][0] >= X and line[1][0] <= X:
            inside.append(line[0][1])
print(*sorted(list(set(inside))))
