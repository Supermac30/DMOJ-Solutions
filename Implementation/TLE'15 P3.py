import sys; input=sys.stdin.readline
def buildLine(counter, size, start):
    """
    :param counter: holds the location in the poem you are in
    :param size: holds the index of the size of the sentence in cycles
    :param start: holds the starting index of the word you are in
    :return: continue, new counter, new size, new start
    """
    #print("TEST: " + sentence[counter] + " " + str(cycles[size]))
    if counter + 1 > length: return False, 0, 0, 0
    if len(sentence[counter][start:]) > cycles[size]:
        print(sentence[counter][start:cycles[size]+start])
        return True, counter, (size+1)%amount, cycles[size]+start

    line = sentence[counter][start:]
    counter += 1
    while counter + 1 <= length and len(line+" "+sentence[counter]) <= cycles[size]:
        line += " "+sentence[counter]
        counter += 1
    print(line)
    return True, counter, (size+1)%amount, 0


cycles = []
amount = int(input())
for i in range(amount):
    cycles.append(int(input()))
sentence = input().split()
length = len(sentence)
cont, counter, size, start = buildLine(0,0,0)
while cont:
    cont, counter, size, start = buildLine(counter, size, start)
