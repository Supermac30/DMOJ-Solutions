"""
  https://dmoj.ca/problem/phantom2
"""
import sys;input=sys.stdin.readline
def createSieve(size):
    sieve = [False, False] + [True] * (size-1)
    for i in range(2, size-1):
        if sieve[i] == True:
            for j in range(i+i, len(sieve), i):
                sieve[j] = False
    return sieve
sieve = createSieve(1000000)
for i in range(int(input())):
    a, b = map(int, input().split())
    print(sieve[a:b].count(True))
