"""
	https://dmoj.ca/problem/ccc03s3
"""
import sys; input = sys.stdin.readline
wood = int(input())
floor = []
row = int(input())
col = int(input())
for _ in range(row):
    floor.append(list(input()[:-1]))


def fix(a, b):
    counter, add = 0, 0
    while len(floor[a])-b != add and floor[a][b+add] == ".":
        floor[a][b+add] = "X"
        add += 1
        counter += 1
    for x in range(add):
        if a+1 < len(floor) and floor[a+1][b+x] == ".":
            change = 0
            while floor[a+1][b+x-change] == "." and b+x-change > -1:
                change += 1
            counter += fix(a+1, b+x-change+1)
        if a-1 > -1 and floor[a-1][b+x] == ".":
            change = 0
            while floor[a-1][b+x-change] == "." and b+x-change > -1:
                change += 1
            counter += fix(a-1, b+x-change+1)
    return counter


areas = []
for i in range(0, row):
    for j in range(0, col):
        if floor[i][j] == ".":
            areas.append(fix(i, j))
areas = sorted(areas, reverse=True)
total = 0
amount = 0
for num in areas:
    if total+num <= wood:
        total += num
        amount += 1
    else:
        break
print(amount, "rooms," if amount != 1 else "room,", wood-total, "square metre(s) left over")
