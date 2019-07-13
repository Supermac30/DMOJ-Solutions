"""
  https://dmoj.ca/problem/rollencrypt
  Holds a tally of the last k characters. This is to avoid recounting every iteration as the last character can be added and first removed.
"""
import sys; input = sys.stdin.readline

k = int(input())
word = input()
string = ""
tally = [0]*26
for i in range(k):
    string+=word[i]
    tally[ord(word[i])-ord("a")]+=1
for i in range(k, len(word)-1):
    shift = tally.index(max(tally))
    string+=chr(((ord(word[i])-ord("a")+shift+1)%26)+ord("a"))
    tally[ord(word[i-k])-ord("a")]-=1
    tally[ord(word[i])-ord("a")]+=1
print(string)
