import sys; input = sys.stdin.readline
class node:
    def __init__(self,name):
        self.parents = []
        self.values = []
        self.name = name

def fix(node, nums,visited):
    if node.name in visited:
        return
    visited.append(node.name)
    temp = node.values
    for num in nums:
        if num not in node.values:
            node.values.append(num)
    for parent in node.parents:
        fix(nodes.get(parent), nums, visited)

nodes = {}
for i in range(int(input())):
    inp = input().split()
    x,y = inp[0],inp[2]
    if x not in nodes:
        nodes[x] = node(x)
    if y.islower():
        nodes[x].values.append(y)
        continue
    if y not in nodes:
        nodes[y] = node(y)
    nodes[y].parents.append(x)

for key,node in nodes.items():
    for parent in node.parents:
        fix(nodes.get(parent), node.values,[])

names = sorted(nodes)
for name in names:
    values = sorted(nodes.get(name).values)
    print(name,"=","{"+str(values)[1:-1].replace(' ','').replace('\'','')+"}")
