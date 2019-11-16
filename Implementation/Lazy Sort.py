"""
	https://dmoj.ca/problem/fhc15c2p1
"""
import sys
input = sys.stdin.readline
for i in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    sort = [nums[0]]
    right = True
    for j in range(1,len(nums)):
        if nums[j] > sort[-1]:
            sort.append(nums[j])
        elif nums[j] < sort[0]:
            sort.insert(0,nums[j])
        elif nums[0] > sort[-1]:
            sort.append(nums[0])
        elif nums[0] > sort[0]:
            sort.insert(0,nums[j])
        else:
            print("Case #"+str(i+1)+": no")
            right = False
            break
    if right:
        print("Case #"+str(i+1)+": yes")
