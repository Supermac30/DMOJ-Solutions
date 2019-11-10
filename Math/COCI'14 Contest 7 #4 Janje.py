"""
    https://dmoj.ca/problem/coci14c7p4
    Solved on paper then hard coded it here
    Remember to subtract 6 from each n in three*n because the number of 2 color permutations are counted multiple times otherwise
"""
from math import factorial
def choose(n, k):
    if n < k:
        return 0
    return factorial(n)/(factorial(k)*factorial(n-k))

N, k = map(int, input().split())
two = int(choose(k ,2))
three = int(choose(k, 3))
if N == 1:
    print(two*2+three*1572858)
elif N == 2:
    print(96*three)
elif N == 3:
    print(2*two + 18*three)
elif N == 4:
    print(2*two + 24570*three)
elif N == 5:
    print(12*three)
elif N == 6:
    print(6*three)
elif N == 7:
    print(96*three)
elif N == 8:
    print(2*two + 1073741820*three)
