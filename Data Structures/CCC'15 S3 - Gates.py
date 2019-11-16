"""
	https://dmoj.ca/problem/ccc15s3
"""
import sys; input = sys.stdin.readline
class node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        
def bst(sortedarr):
    if sortedarr == []:
        return None
    mid = len(sortedarr)//2
    root = node(sortedarr[mid])
    root.left = bst(sortedarr[:mid])
    root.right = bst(sortedarr[mid+1:])
    return root
"""
def preorder(root):
    if root == None:
        print("up")
        return
    print(root.name)
    preorder(root.left)
    preorder(root.right)
    return
"""
def minValue(root):
    check = root
    while check.left != None:
        check = check.left
    return check

counter = 0

def delete(root,val):
    if root == None: return root
    if val < root.name:
        root.left = delete(root.left,val)
    elif val > root.name:
        root.right = delete(root.right,val)
    else:
        if root.left == None:
            store = root.right
            root = None
            return store
        if root.right == None:
            store = root.left
            root = None
            return store
        store = minValue(root.right)
        root.name = store.name
        root.right = delete(root.right, store.name)
    return root

def search(root):
    global docks
    global counter
    global plane
    if root == None:
        return False
    if root.name == plane:
        docks = delete(docks,root.name)
        counter += 1
        return True
    if root.name > plane:
        return search(root.left)
    if search(root.right) == False:
        docks = delete(docks,root.name)
        counter += 1
        return True
    return True
    
docks = bst(list(range(1,int(input())+1)))
for i in range(int(input())):
    plane = int(input())
    if not search(docks):
        break

print(counter)