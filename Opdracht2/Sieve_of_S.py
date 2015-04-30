import sys
import time
import math

count = len(sys.argv) - 1
argumentList = sys.argv

fileName = argumentList.pop(count)
upperLimit = int(argumentList.pop(count - 1))

#Create the full numbers list
primes = [True] * upperLimit

T1 = time.perf_counter()

for i in range(1, upperLimit) :
    for j in range(1, upperLimit) :
        if i + j + (2 * i * j) >= upperLimit :
            break
        primes[i + j + (2 * i * j)] = False

T2 = time.perf_counter()

#2 will not be included, include it automatically
file = open(fileName, 'w')
print(2, sep='\n', file=file)
count = 1

for i in range(1, upperLimit) :
    if (2 * i + 1 > upperLimit) :
        break
    if primes[i] :
        count = count + 1
        print(2 * i + 1, sep='\n', file=file)

print('Found %d Prime numbers smaller than %d in %d sec.' % (count, upperLimit, T2 - T1))
print('--------------------------------------------')
