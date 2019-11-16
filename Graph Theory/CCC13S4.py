"""
  https://dmoj.ca/problem/ccc13s4
"""
import sys; input = sys.stdin.readline
N, M = map(int, input().split())
students = {}
for i in range(N):
    students[i+1]=[]
for _ in range(M):
    x, y = map(int, input().split())
    students[x].append(y)

def dfs(a, b):
    stack = students[a].copy()
    seen = set()
    while stack:
        student = stack.pop(-1)
        if student == b:
            return True
        if student in seen:
            continue
        seen.add(student)
        stack.extend(students[student])
    return False

p, q = map(int, input().split())
if dfs(p, q):
    print("yes")
elif dfs(q, p):
    print("no")
else:
    print("unknown")
