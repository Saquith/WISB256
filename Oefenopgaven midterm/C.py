import math

v = int(input()) #vuurkracht    = x m/s
g = int(input()) #zwaartekracht = x m/s²
l = int(input()) #afstand       = x m

alpha = math.asin((l*g) / (v**2)) / 2

print("{0:.2f}".format(alpha))
