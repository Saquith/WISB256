import math
import bisection

divider = '--------------------------------------'
print('findRoot testing:')
print(divider)

print(bisection.findRoot(lambda x:x*(x-1),0,3,.1))
print(bisection.findRoot(lambda x:x**2,0,3,.1))
print(bisection.findRoot(lambda x:math.cos(x),0,3,.1))

print(divider)
print('findAllRoots testing:')
print(divider)

print(bisection.findAllRoots(lambda x:x**2-2,-2,2,.1))
print(bisection.findAllRoots(lambda x:math.sin(x),0.1,9,.1))

print(divider)

print("Job's done!")
