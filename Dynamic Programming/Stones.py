"""
  This is a dynamic programming solution to a game theory problem
  https://dmoj.ca/problem/dpk
"""
import sys; input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
positions = [False] * k

for i in range(k):
    winning = False
    for j in a:
        if j > i + 1:
            continue
        # if every position you point to is a winning position then you are in a losing position
        if not positions[i-j]:
            winning = True
            break
    if i + 1 in a:
        winning = True
    positions[i] = winning

print("First" if positions[-1] else "Second")
