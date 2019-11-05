"""
  https://dmoj.ca/problem/dwite11c3p5
  I solved this problem by simply brute forcing all posibilities, given the large time frame and
  small input, and printing if the value is ever false.
"""
import sys;input=sys.stdin.readline

letters = "abcdefghij"


def fix(statement):
    return statement.replace("v", " or ").replace("^", " and ").replace("~", " not ").replace("T", " True ").replace("F", " False ")


def brute(statement, i, boolean):
    statement = statement.replace(letters[i], boolean)
    if not (set(letters) & set(statement)) or i + 1 == len(letters):
        return eval(fix(statement))
    return brute(statement, i+1, "T") and brute(statement, i+1, "F")


#handle inp and out
for i in range(5):
    for i in range(3):
        statement = input()
        if brute(statement, 0, "T") and brute(statement, 0, "F"):
            print("Y", end='')
        else:
            print("N", end='')
    print()
