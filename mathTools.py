#!/usr/local/bin/python

def nextPrime(primeList):
    if primeList==[]:
        return [2]

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

# from problem10.py
def primesLessThan(targetPrime):
    primeList = [2]
    allPrimes = set([2] + range(3,int(targetPrime),2)) #start with 2 and higher odd numbers
    while True:
        primeList = nextPrimeFromList(primeList,allPrimes)
        latest = primeList[-1]
        elim = set(range(latest*latest,int(targetPrime),latest))
        if len(elim)==0:
            break
        allPrimes -= elim
    return list(allPrimes)


def isprime(n):
    plist = primesLessThan(int(n**0.5)+1)
    prime = True
    for p in plist:
        if not n==p and n%p==0:
            prime = False
            break
    return prime


def primefactor(num,plist=[]):
#
# trial division algorithm
# http://en.wikipedia.org/wiki/Trial_division
#
    if len(plist)==0:
        #plist = primesLessThan(num)
        plist = primesLessThan(int(num**0.5)+1)
    #print num,plist

    flist = []
    for p in plist:
        #if not num%p==0: continue
        if p*p > num: break
        
        while num%p ==0:
            flist.append(p)
            num /= p
    if num > 1:
        flist.append(num)

    return flist


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

