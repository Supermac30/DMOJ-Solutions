#fastest way to get input, note input() will now read new line characters '\n'
import sys; input=sys.stdin.readline

#Fastest way to check if a value is prime
def isPrime(n):
    if n == 1 or (n%2 == 0 and n != 2):
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

#Creates the Sieve of Eratosthenes, finding primes in a range of values
def sieve(size):
    sieve = [True] * (size-1)
    for i in range(size-1):
        if sieve[i] == True:
            for j in range(2*i+2, len(sieve), i+2):
                sieve[j] = False
    return [False] + sieve

#returns the prime factors of n
def primeFactors(n):
    if n <= 0:
        return []
    fact = []
    while n%2 == 0:
        n //= 2
        fact.append(2)
    check = 3
    while n != 1:
        while n % check == 0:
            n //= check
            fact.append(check)
        check += 2
    return fact

#Returns the factors of n
def factors(n):
    fact = [n]
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            fact.append(k)
            fact.append(n//k)
    return fact

#bfs through a graph, works if there exists a function 'children' returning adjacent nodes
def bfs(start, end, graph):
    from collections import deque
    queue = deque(children(start))
    amount = len(queue)
    counter = 0
    seen = set()
    while queue:
        if amount == 0:
            amount = len(queue)
            counter += 1
        amount -= 1
        check = queue.popleft()
        if check in seen:
            continue
        seen.add(check)
        if check == end:
            return counter
        queue.extend(children(check))
    return -1

#return the distance from the start node to every other node in a graph
def bfsAll(start, graph):
    from collections import deque
    queue = deque(children[start])
    amount = len(queue)
    counter = 1
    seen = set()
    distances = [-1]*len(graph)
    while queue:
        if amount == 0:
            amount = len(queue)
            counter += 1
        check = queue.popleft()
        amount -= 1
        if check in seen:
            continue
        seen.add(check)
        graph[check-1] = counter
        queue.extend(children[check])
    return distances

#dfs through a graph, works if there exists a function 'children' returning adjacent nodes
def dfs(start, end, graph):
    stack = chlidren(start)
    seen = set()
    while queue:
        check = stack.pop()
        if check in seen:
            continue
        seen.add(check)
        if check == end:
            return True
        stack.extend(children(check))
    return False

#Fastest Fib algorithm
fibs = {1:1, 2:1}
def fib(n):
    if n in fibs:
        return fibs.get(n)
    if n % 2 == 0:
        fibs[n] = fib(n//2) * (2*fib((n//2) + 1) - fib(n//2))
        return fibs.get(n)
    fibs[n] = (fib(((n-1)//2) + 1)**2 + fib((n-1)//2)**2)
    return fibs.get(n)

#Solves 0-1 Knapsack
def knapsack(values, weights, maxWeight):
    A = [[0]*(maxWeight+1)]
    for i in range(len(values)):
        A.append([-1]*(maxWeight+1))
    for i in range(1, len(values)+1):
        for j in range(maxWeight+1):
            if j >= weights[i-1]:
                A[i][j] = max(A[i-1][j], values[i-1] + A[i-1][j-weights[i-1]])
            else:
                A[i][j] = A[i-1][j]
    return A[-1][-1]

#Implements Binary Search
def binSearch(sortedarr, value, left = 0, right = -1):
    if right == -1:
        right = len(sortedarr)
    if right < left:
        return -1
    mid = (left+right)//2
    check = sortedarr[mid]
    if check == value:
        return mid
    if check > value:
        return binSearch(sortedarr, value, left, mid)
    return binSearch(sortedarr, value, mid, right)

#Implements a Binary Search Tree which allows for the searching through a sorted array and inserting into a sorted array in O(log n) time
class node():
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
class BST():
    def __init__(self, sortedarr):
        self.root = self.bst(sortedarr)
    def bst(self, sortedarr):
        if sortedarr == []:
            return None
        mid = len(sortedarr)//2
        root = node(sortedarr[mid])
        root.left = self.bst(sortedarr[:mid])
        root.right = self.bst(sortedarr[mid+1:])
        return root
    def preorder(self, root=-1):
        if root == -1:
            root = self.root
        if root == None:
            print("up")
            return
        print(root.name)
        self.preorder(root.left)
        self.preorder(root.right)
        return
    def minValue(self, root=-1):
        if root == -1:
            root = self.root
        check = root
        while check.left != None:
            check = check.left
        return check
    def delete(self, val, root=-1):
        if root == -1:
            root = self.root
        if root == None: return root
        if val < root.name:
            root.left = self.delete(val, root.left)
        elif val > root.name:
            root.right = self.delete(val, root.right)
        else:
            if root.left == None:
                store = root.right
                root = None
                return store
            if root.right == None:
                store = root.left
                root = None
                return store
            store = self.minValue(root.right)
            root.name = store.name
            root.right = self.delete(store.name, root.right)
        return root
    def search(self, val, root=-1):
        if root == -1:
            root = self.root
        if root is None or root.name == val:
            return root
        if root.name < val:
            return self.search(val, root.right)
        return self.search(val, root.left)
