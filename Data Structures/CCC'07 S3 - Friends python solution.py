import sys
loops = []
def fixdata(a,b):
    for loop in loops:
        if loop[-1] == a: loop.append(b);return
        elif loop[0] == b: loop[:0]=[a];return
    loops.append([a,b])
def find(a,b):
    for loop in loops:
        faster = set(loop)
        try:print("Yes", (loop.index(b)-loop.index(a)-1)%(len(loop)-1));return
        except Exception:continue
    print("No")
for i in range(int(input())):
    a,b = sys.stdin.readline().split()
    fixdata(a,b)
a,b = sys.stdin.readline().split()
while a != '0':
    find(a,b)
    a,b = sys.stdin.readline().split()
