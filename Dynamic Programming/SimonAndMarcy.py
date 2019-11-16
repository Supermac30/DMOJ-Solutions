"""
  https://dmoj.ca/problem/valday15p2
"""
# Knapsack 0-1
import sys; input = sys.stdin.readline
# handle input
C, M = map(int, input().split())
V, W = [], []
for i in range(C):
    v, w = map(int, input().split())
    V.append(v)
    W.append(w)

A = [[]]
for i in range(M+1):
    A[0].append(0)
for i in range(C):
    A.append([-1]*(M+1))
for i in range(1, C+1):
    for j in range(M+1):
        if j >= W[i-1]:
            A[i][j] = max(A[i-1][j], V[i-1] + A[i-1][j-W[i-1]])
        else:
            A[i][j] = A[i-1][j]
print(A[-1][-1])
