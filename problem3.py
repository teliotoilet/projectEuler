#!/usr/local/bin/python
from mathTools import *

#testNumber = 13195
testNumber = 600851475143

primeList = [2]
primeFactors = []
curValue = testNumber
while curValue > 1:
    print primeList
    largestPrime = primeList[-1]
    if curValue%largestPrime==0:
        curValue /= largestPrime
        primeFactors.append(largestPrime)
    primeList = nextPrime(primeList)

    if max(primeList) > testNumber:
        print 'how did this happen?',primeList[-1],testNumber
        break

print 'Prime factors of',testNumber,':',primeFactors
