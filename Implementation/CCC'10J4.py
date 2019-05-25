import sys;input=sys.stdin.readline
inp = list(map(int,input().split()))
def period(size):
    if size == len(diff):
        print(len(diff))
        return
    sub = diff[:size+1]
    answer = True
    for i in range(0,len(diff),len(sub)):
        if len(diff)-i < len(sub):
            if sub[:len(diff)-i] != diff[i:i+len(sub)]:
                answer = False
            break
        if diff[i:i+len(sub)] != sub:
            answer = False
    if answer:
        print(len(sub))
        return
    period(size+1)

while inp[0] != 0:
    if inp[0] == 1:
        print(0)
        inp = list(map(int,input().split()))
        continue
    diff = [inp[i]-inp[i-1] for i in range(2,inp[0]+1)]
    period(0)
    inp = list(map(int,input().split()))
