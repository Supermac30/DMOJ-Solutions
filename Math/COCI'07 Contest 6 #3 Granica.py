"""
	https://dmoj.ca/problem/coci07c6p3
"""
import sys; input = sys.stdin.readline
nums = []
smallest = 1000000000
# input handling
for i in range(int(input())):
    nums.append(int(input()))
    if nums[-1] < smallest:
        smallest = nums[-1]

# make all numbers as small as possible
for i in range(len(nums)):
    nums[i] -= smallest
nums = list(set(nums))


def factors(n):
    # returns the factors of n
    fact = [n]
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            fact.append(k)
            fact.append(n//k)
    return fact


first = True
if nums == [0]:
    common = range(2, smallest+1)
elif 1 in nums:
    common = []
else:
    # finds the common factors of all the input
    common = []
    for num in nums:
        if num == 0:
            continue
        if not common:
            if not first:
                common = []
                break
            common = set(factors(num))
            first = False
        else:
            common = set(factors(num)).intersection(common)
common = map(str, common)
print(' '.join(common))
