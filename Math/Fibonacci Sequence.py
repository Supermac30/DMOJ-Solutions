"""
  https://dmoj.ca/problem/fibonacci
  using the fact that:
 - fib(2x) = fib(x)*(fib(x+1)-fib(x))
 - fib(2x+1) = (fib(x+1))^2 + fib(x)^2
 - (a*b) mod x = (a modx * b modx) modx
  a recursive solution with memorisation can find the answer very quickly
"""
fibs = {1:1, 2:1}
def fib(n):
    if n in fibs:
        return fibs.get(n)
    if n % 2 == 0:
        fibs[n] = fib(n//2) * (2*fib((n//2) + 1) - fib(n//2)) % 1000000007
        return fibs.get(n)
    fibs[n] = (fib(((n-1)//2) + 1)**2 + fib((n-1)//2)**2) % 1000000007
    return fibs.get(n)

print(fib(int(input())) % 1000000007)
