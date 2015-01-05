#!/usr/local/bin/python

def nextPrime(primeList):
    nextNum = max(primeList)
    while True:
        nextNum += 1
        if not any([nextNum%val==0 for val in primeList]):
            primeList.append(nextNum)
            break
    return primeList


