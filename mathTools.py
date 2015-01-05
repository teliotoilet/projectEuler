#!/usr/local/bin/python

def nextPrime(primeList):
    nextNum = max(primeList)
    if nextNum%2==0: #even
        nextNum -= 1 #test consecutive odd numbers only for efficiency
    while True:
        #nextNum += 1
        nextNum += 2 
        if not any([nextNum%val==0 for val in primeList]):
            primeList.append(nextNum)
            break
    return primeList


