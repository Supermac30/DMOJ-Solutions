"""
  https://dmoj.ca/problem/dpl
"""
import sys; input = sys.stdin.readline
N = int(input())
values = list(map(int, input().split()))
dp = []
for i in range(N):
    dp.append([None]*N)
for i in range(N):
    isMin = (N%2)-(i%2)==0
    for j in range(N):
        if i+j >= N:
            break
        if i == 0:
            dp[j][j] = values[j]*((-1)**(1+(N%2)))
        elif isMin:
            dp[j][i+j] = min(-values[j]+dp[j+1][i+j], -values[j+i]+dp[j][i+j-1])
        else:
            dp[j][i+j] = max(values[j]+dp[j+1][i+j], values[j+i]+dp[j][i+j-1])
print(dp[0][-1])
