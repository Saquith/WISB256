import sys
import math

argumentList = sys.argv

fileName = argumentList.pop()

file = open(fileName, 'r')
const = 0.6601618

line = file.readline()
percentage = 0
lineCount = 0
previousLine = -1
twinCount = 0

while (line != '') :
    lineCount += 1
    #printing progress
    #currentPercentage = int(lineCount/(5761455/100))
    #if (percentage != currentPercentage) :
    #    percentage = currentPercentage
    #    print(percentage)

    #doing calculations
    if (previousLine == int(line) - 2) :
        twinCount += 1

    #read new line
    previousLine = int(line)
    line = file.readline()

log = math.log(previousLine)
lineFormula = previousLine / log
twinFormula = 2 * const * previousLine / math.pow(log, 2)

divider = '---------------------------------'

print('Largest Prime = %d' % previousLine)
print(divider)
print('pi(N)        = %d' % lineCount)
print('N/log(N)     = %s' % lineFormula)
print('ratio        = %s' % (lineCount / lineFormula))
print(divider)
print('pi_2(N)      = %d' % twinCount)
print('2CN/log(N)^2 = %s' % twinFormula)
print('ratio        = %s' % (twinCount / twinFormula))
