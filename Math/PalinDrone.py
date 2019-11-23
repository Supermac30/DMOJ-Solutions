"""
  https://dmoj.ca/problem/gfssoc3s3
"""
n = int(input())-1
if n == 0:
    total = 9
elif n >= 18:
    total = 999999998
else:
    half0 = int((n-1)/2)
    half1 = int(n/2)
    total = ((10**(half0+1))*(1+10**(half1-half0))-2)%1000000000
print(total)
