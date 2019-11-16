"""
	https://dmoj.ca/problem/coci13c2p3
"""
import sys; input = sys.stdin.readline

def move(word):
    times = len(word)// 2
    for i in range(times):
        word.insert(2*i+1,word[-1])
        del word[-1]
    return word

def period(length):
    arr = [i for i in range(length)]
    original = arr.copy()
    arr = move(arr)
    counter = 1
    while arr != original:
        arr = move(arr)
        counter += 1
    return counter

blinks = int(input())
inp = list(input()[:-1])
spin = -blinks%(period(len(inp)))
for i in range(spin):
    inp = move(inp)
print(''.join(inp))