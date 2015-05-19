N = int(input())
paint = 0
meadow = []

for i in range(0, N) :
    meadow.append(input())

for i in range(0, len(meadow)) :
    for j in range (0, len(meadow[i])) :
        if meadow[i][j] == '#' :
            paint += 5

print('Om de hekjes in dit weiland te verven heb je %s liter verf nodig' % paint)
