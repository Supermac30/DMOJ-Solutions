"""
  https://dmoj.ca/problem/dph
"""
import sys; input = sys.stdin.readline
H, W = map(int, input().split())
dp = []
for i in range(H):
    inp = list(input()[:-1])
    temp = []
    for char in inp:
        if char == '.':
            temp.append(0)
        else:
            temp.append(None)
    dp.append(temp)
for i in range(H):
    for j in range(W):
        if dp[i][j] == None:
            continue
        if i+j==0:
            dp[i][j] = 1
            continue
        up = 0
        left = 0
        if i-1 >= 0 and dp[i-1][j] != None:
            up = dp[i-1][j]
        if j-1 >= 0 and dp[i][j-1] != None:
            left = dp[i][j-1]
        dp[i][j] = up + left
if dp[-1][-1] == None:
    print(0)
else:
    print(dp[-1][-1]%(7+(10**9)))
