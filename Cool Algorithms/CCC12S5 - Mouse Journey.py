"""
  https://dmoj.ca/problem/ccc12s5
"""
import sys; input=sys.stdin.readline
R, C = map(int, input().split())
dp = []
for i in range(R):
    dp.append([0]*C)
if C == 0:
    print(0)
else:
    dp[0][0] = 1
    for i in range(int(input())):
        x, y = map(int, input().split())
        dp[x-1][y-1] = None
    for i in range(R):
        for j in range(C):
            if (i == 0 and j == 0) or dp[i][j] == None:
                continue
            if dp[i-1][j] is None and dp[i][j-1] is None:
                continue
            if dp[i-1][j] is None:
                dp[i][j] = dp[i][j-1]
            elif dp[i][j-1] is None:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[-1][-1])
