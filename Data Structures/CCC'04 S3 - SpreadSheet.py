import sys;input=sys.stdin.readline
class node():
    def __init__(self, value):
        self.value = None
        if value[0].isdigit():
            self.value = int(value)
        else:
            self.children = value.split("+")
    def amount(self):
        if self.value == None:
            total = 0
            for child in self.children:
                total+= nodes.get(child).amount()
            self.value = total
        return self.value
alpha = ['A','B','C','D','E','F','G','H','I','J']
nodes = {}
grid = []
for i in range(10):
    grid.append(input().split())
for i in range(10):
    for j in range(9):
        nodes[alpha[i]+str(j+1)] = node(grid[i][j])
for i in range(10):
    for j in range(9):
        try:
            print(nodes.get(alpha[i]+str(j+1)).amount(),end=' ')
        except:
            print("*",end=' ')
    print()
