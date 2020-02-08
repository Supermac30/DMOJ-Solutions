"""
  https://dmoj.ca/problem/ccc15j5
"""
mem = {}
def amount(n, k, start):
    if k == 1 or n == k:
        return 1
    total = 0
    for i in range(start, n//k + 1):
        if (n-i, k-1, i) in mem:
            total += mem.get((n-i, k-1, i))
            continue
        val = amount(n-i, k-1, i)
        mem[(n-i, k-1, i)] = val
        total += val
    return total
print(amount(int(input()), int(input()), 1))
