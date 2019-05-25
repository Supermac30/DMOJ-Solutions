import sys, math
input = sys.stdin.readline
try:
    amount = int(input())
except Exception:
    amount = 0
mod = 2**32
for i in range(amount):
    number = int(input())
    if number <= 33:
        print(math.factorial(number)%mod)
    else:
        print(0)
