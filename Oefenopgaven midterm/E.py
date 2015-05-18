r1 = list(input())
r2 = list(input())
r3 = list(input())

def win(i, winCondition) :
    if not winCondition :
        print('Player %s wins' % i)
    return True

def checkRows(l, winCondition) :
    if l[0] != '0' and l[0] == l[1] and l[0] == l[2] :
        return win(l[0], winCondition)

def checkColums(i, winCondition) :
    if r1[i] != '0' and r1[i] == r2[i] and r1[i] == r3[i] :
        return win(r1[i], winCondition)

def checkAcross(i, winCondition) :
    if r1[abs(0 - i)] != '0' and r1[abs(0 - i)] == r2[abs(1 - i)] and r1[abs(0 - i)] == r3[abs(2 - i)] :
        return win(r1[abs(0 + i)], winCondition)

w1 = checkRows(r1, False)
w2 = checkRows(r2, w1)
w3 = checkRows(r3, w1 or w2)
rows = w1 or w2 or w3
w4 = checkColums(0, rows)
w5 = checkColums(1, rows or w4)
w6 = checkColums(2, rows or w5)
rowscolums = rows or w4 or w5 or w6
w7 = checkAcross(0, rowscolums)
w8 = checkAcross(2, rowscolums or w7)
win = rowscolums or w7 or w8
if not win :
    print('No winner')
