"""
  https://dmoj.ca/problem/dwite09c7p5
"""
def isOn(n, k):
    if k%2==0 or n == 0:
        return False
    for i in range(2, n+1):
        if k%(2**i) <= 2**(i-1):
                return False
    return True
for i in range(5):
    n, k = map(int, input().split())
    print("ON" if isOn(n, k) else "OFF")
