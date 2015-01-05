#!/usr/local/bin/python

#testNumber = 13195
testNumber = 600851475143

def nextPrime(primeList):
    nextNum = max(primeList)
    while True:
        nextNum += 1
        if not any([nextNum%val==0 for val in primeList]):
            primeList.append(nextNum)
            break
    return primeList

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
