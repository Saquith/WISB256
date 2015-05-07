import sys
import math
import random

count = len(sys.argv) - 1
argumentList = sys.argv

#functions
def drop_needle(L) : #aslongasitsnotsoap
    x = random.random()
    y = random.random()
    a = random.vonmisesvariate(0,0)
    x2 = x + L * math.cos(a)
    y2 = y + L * math.sin(a)

    #check if it crosses the line
    if (x < 0 and x2 >= 0) or (x >= 0 and x2 < 0) :
        return True
    if (x < 1 and x2 >= 1) or (x >= 1 and x2 < 1) :
        return True
    return False

#body
if (count < 2) :
    sys.exit('Use: python estimate_pi.py N L')

#check if a seed was given
if (count == 3) :
    random.seed(int(argumentList.pop()))

L = float(argumentList.pop())
N = int(argumentList.pop())

count = 0
#from 0 to N, so we get N repeats
for i in range(0, N) :
    if(drop_needle(L)) :
        count += 1
approxPi = -1
if L > 1 :
    approxPi = 2*L / (count/N - 1) - (2/(count/N - 1) * (math.sqrt(L**2 - 1) + math.asin(1/L)))
else :
    approxPi = 2*L * N / count

print('%d hits in %d tries' % (count, N))
print('Pi = %s' % approxPi)
