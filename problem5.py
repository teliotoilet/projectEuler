#!/usr/local/bin/python
from mathTools import *

#maxInteger = 10
maxInteger = 20

primeList = [2]
while primeList[-1] <= maxInteger:
    primeList = nextPrime(primeList)
primeList = primeList[:-1]
print primeList

cumProd = 1
for val in primeList:
    cumProd *= val
print 'initial cumultaive product :',cumProd

for i in range(4,maxInteger+1):
    while not cumProd%i==0:
        print ' ',i,'not a factor of',cumProd
        for pfac in primeList:
            if i%pfac==0:
                cumProd *= pfac
                print '   ',pfac,'is a factor... new cumProd',cumProd
print 'final cumulative product :',cumProd
