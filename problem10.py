#!/usr/local/bin/python
from mathTools import *

targetPrime = 2000000

# SLOW
#primeList = [2]
#i = 1
#while primeList[-1] < targetPrime:
#    i += 1
#    print '#',i,':',primeList[-1]
#    primeList = nextPrime(primeList)

primeList = [2]
allPrimes = set([2] + range(3,targetPrime,2)) #start with 2 and higher odd numbers
#while not primeList==allPrimes:
while True:
    primeList = nextPrimeFromList(primeList,allPrimes)
    latest = primeList[-1]
    print 'removing multiples of',latest
    # SLOW
    #for mult in range(latest*2,targetPrime,latest): #elim multiples of latest prime
    #    try:
    #        allPrimes.remove(mult)
    #        print '  removed',mult
    #    except ValueError:
    #        pass
    elim = set(range(latest*latest,targetPrime,latest))
    if len(elim)==0:
        print 'no more primes to remove!'
        break

    allPrimes -= elim
    print 'new size :',len(allPrimes)

print 'sum of primes below',targetPrime,':',sum(allPrimes)
