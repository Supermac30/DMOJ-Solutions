"""
  https://dmoj.ca/problem/bf4hard
  Uses KMP to find the location of the substring
"""
import sys;input=sys.stdin.readline
def buildLPS(word):
    start = 0
    lps = [0]*len(word)
    check = 1
    while check != len(word):
        if word[check] == word[start]:
            lps[check] = start + 1
            start += 1
        else:
            if start != 0:
                start = lps[start-1]
                check -= 1
        check += 1
    return lps

def find(search, pattern):
    lps = buildLPS(pattern)
    P, S = len(pattern), len(search)
    check = 0
    loc = 0
    while check != S:
        if pattern[loc] == search[check]:
            check += 1
            loc += 1
        else:
            if loc != 0:
                loc = lps[loc-1]
            else:
                check += 1
        if loc == P:
            return check-P
        if check == S:
            return -1
print(find(input()[:-1], input()[:-1]))
