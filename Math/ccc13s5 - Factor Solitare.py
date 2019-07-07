"""
  https://dmoj.ca/problem/ccc13s5
  Finds the number with the lowest cost that isn't prime
"""
import math
cost = 0


def poss(x):
    global cost
    if x == 1:
        return
    for i in range(int(x/2),x):
        if i%(x-i) == 0 and (not isPrime(i) or i <= 2):
            cost+=i/(x-i)
            poss(i)
            return


def isPrime(x):
    for i in range(1, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


poss(int(input()))
print(int(cost))
