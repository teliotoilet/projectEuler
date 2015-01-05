#!/usr/local/bin/python
from mathTools import *

nprimes = 10001

primeList = [2]
for i in range(1,nprimes):
    print '#',i,':',primeList[-1]
    primeList = nextPrime(primeList)

assert(len(primeList)==nprimes)
print '#',i+1,':',primeList[-1]
