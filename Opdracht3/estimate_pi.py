import sys
import random

count = len(sys.argv) - 1
argumentList = sys.argv

#functions
#def run() :

#body
if (count < 2) :
    sys.exit('Use: python estimate_pi.py N L')
    
L = int(argumentList.pop(count))
N = int(argumentList.pop(count - 1))

if (L > 1) :
    sys.exit('AssertionError: L should be smaller than 1')
    

# uniform in [0,1]
x = random.random()
# uniform in [0,2\pi]
a = random.vonmisesvariate(0,0)
