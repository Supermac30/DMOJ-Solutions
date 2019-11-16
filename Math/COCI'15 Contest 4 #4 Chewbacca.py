"""
    I'm seriously proud of this code.
    Anything is possible if you stay up till 3 am.
	https://dmoj.ca/problem/coci15c4p4
"""

import sys,math;input=sys.stdin.readline
def fix(level): return (1-(K**level))/(1-K)
def distance(a,b):
    levelA = int(math.log(a*(K-1),K))
    levelB = int(math.log(b*(K-1),K))
    locA = a-fix(levelA)-1
    counter = levelB-levelA
    locB = math.ceil((b-fix(levelB))/(K**counter))-1
    while locB != locA:
        counter += 2
        locA //= K
        locB //= K
    return counter
N,K,Q = map(int,input().split())
if K == 1:
    for i in range(Q):
        a,b = map(int,input().split())
        print(abs(b-a))
else:
    for i in range(Q):
        a,b = map(int,input().split())
        if b < a: a,b = b,a
        print(distance(a,b))
