"""
  https://dmoj.ca/problem/ccc13s3
"""
import sys; input = sys.stdin.readline
T = int(input())
numGames = int(input())
scores = [0,0,0,0]
allGames = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
for i in range(numGames):
    a, b, s0, s1 = map(int, input().split())
    if s0 > s1:
        scores[a-1] += 3
    elif s1 > s0:
        scores[b-1] += 3
    else:
        scores[a-1] += 1
        scores[b-1] += 1
    if (a-1, b-1) in allGames:
        allGames.remove((a-1, b-1))
    else:
        allGames.remove((b-1, a-1))

numPoss = 0
def findAll(scores, played):
    global numPoss
    if len(played) == 0:
        if scores[T-1] > max(scores[:T-1]+scores[T:]):
            numPoss += 1
        return None
    play = played.pop(0)
    scores[play[0]] += 3
    findAll(scores[:], played[:])
    scores[play[0]] -= 3
    scores[play[1]] += 3
    findAll(scores[:], played[:])
    scores[play[0]] += 1
    scores[play[1]] -= 2
    findAll(scores[:], played[:])
    return None


findAll(scores, allGames)
print(numPoss)
