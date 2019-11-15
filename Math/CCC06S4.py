"""
    https://dmoj.ca/problem/ccc06s4
    All groups are latin squares
"""
N = int(input())
while N != 0:
    square = []
    for i in range(N):
        square.append(input().split())
    isLatin = True
    for i in range(N):
        if len(set(square[i])) != N or len(set([square[j][i] for j in range(N)])) != N:
            isLatin = False
            break
    print("yes" if isLatin else "no")
    N = int(input())
