"""
  https://dmoj.ca/problem/ccc96s5
"""
def binSearch(arr, val, start, end):
    mid = (end+start)//2
    midVal = arr[mid]
    if start == end - 1:
        if midVal != val:
            return -1
        return mid
    elif val <= midVal:
        return binSearch(arr, val, mid, end)
    else:
        return binSearch(arr, val, start, mid)

def solve(X, Y):
    largest = 0
    for i in range(len(X)):
        if i == 0 or X[i] != X[i-1]:
            val = binSearch(Y, X[i], 0, len(Y))
            if val - i > largest:
                largest = val - i
    return str(largest)

for i in range(int(input())):
    input()
    print("The maximum distance is " + str(solve(list(map(int, input().split())), list(map(int, input().split())))))
