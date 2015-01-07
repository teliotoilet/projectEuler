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

# used for Sieve of Erastosthenes
def nextPrimeFromList(primeList,candidates):
    for nextNum in candidates:
        if nextNum in primeList: 
            continue
        if not any([nextNum%val==0 for val in primeList]):
            primeList.append(nextNum)
            break
    return primeList

def cumProd(arr):
    prod = 1
    for val in arr:
        prod *= val
    return prod

def readGrid(fname):
    import numpy as np
    data = []
    with open(fname,'r') as f:
        for line in f:
            data.append([int(val) for val in line.split()])
    return np.array(data)

