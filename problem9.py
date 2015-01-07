#!/usr/local/bin/python
from math import *

targetValue = 1000

def isInt(f):
    return f-int(f)==0

a = 3
while a < targetValue:
    a += 1
    b = a
    while b < targetValue:
        b += 1
        c = sqrt(a*a+b*b)
        if isInt(c):
            break
    if b==targetValue:
        continue
    print a,b,c, a+b+c

    s = a+b+c
    if s==targetValue or isInt(targetValue/s):
        break

scaling = targetValue/s
a *= scaling
b *= scaling
c *= scaling
assert(a*a + b*b - c*c == 0)
print 'Product of a, b, and c summing to',targetValue,':',a*b*c
print '  with the triplet',a,b,c

