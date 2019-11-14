"""
  https://dmoj.ca/problem/ccc00s4
"""
import sys; input=sys.stdin.readline
dist = int(input())
amounts = [int(input()) for i in range(int(input()))]
dp = [5280]*(dist+1)
dp[0] = 0
for i in range(dist+1):
    for amount in amounts:
        if i >= amount:
            dp[i] = min(dp[i], dp[i-amount]+1)
if dp[-1] == 5280:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in {} strokes.".format(dp[-1]))
