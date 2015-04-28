import sys
import time

count = len(sys.argv) - 1
argumentList = sys.argv

#eventual running code
#fileName = argumentList.pop(count)
#upperLimit = int(argumentList.pop(count - 1))

#debug code
fileName = 'test.dat'
upperLimit = 10000

result = []
T1 = time.perf_counter()

#for i in range(1, upperLimit)
    

T2 = time.perf_counter()

print('Found %d Prime numbers smaller than %d in %d sec.' % (len(result), upperLimit, T2 - T1))
