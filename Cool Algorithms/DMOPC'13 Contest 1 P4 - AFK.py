import sys;input=sys.stdin.readline
    
for times in range(int(input())):
    house = []
    l,w = map(int,input().split())
    for i in range(w):
        house.append(input()[:-1])
    count = 0
    found = False
    while count < 60:
        for i in range(w):
            for j in range(l):
                if house[i][j] == "C":
                    new = [[i,j+1],[i,j-1],[i-1,j],[i+1,j]]
                    poss = []
                    for p in new:
                        if not (p[0] < 0 or p[1] <0 or p[0] > w-1 or p[1] > l-1):
                            poss.append(p)
                    for p in poss:
                        if house[p[0]][p[1]] == "W":
                            found = True
                            break
                        if house[p[0]][p[1]] == 'O':
                            temp = list(house[p[0]])
                            temp[p[1]] = "T"
                            house[p[0]] = ''.join(temp)
                    temp = list(house[i])
                    temp[j] = "X"
                    house[i] = ''.join(temp)
                if found:
                    break
            if found:
                break
        count += 1
        if found:
            break
        for i in range(len(house)):
            house[i] = house[i].replace("T","C")
    if count >= 60:
        print("#notworth")
    else:
        print(count)
