import sys
import time
import math

argumentList = sys.argv

fileName = argumentList.pop()
upperLimit = int(argumentList.pop())

#Create the full numbers list
primes = [True] * upperLimit

T1 = time.perf_counter()

for i in range(2, int(math.sqrt(upperLimit))) :
    for j in range(i, upperLimit) :
        # i squared, as j starts as i.
        if i * j >= len(primes) :
            break
        primes[i * j] = False

T2 = time.perf_counter()

#1 is not prime
primes[1] = False

file = open(fileName, 'w')
count = 0
for i in range(1, len(primes)) :
    if primes[i] :
        count = count + 1
        print(i, sep='\n', file=file)

print('Found %d Prime numbers smaller than %d in %s sec.' % (count, upperLimit, T2 - T1))
print('--------------------------------------------')
