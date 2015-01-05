#!/usr/local/bin/python

maxNumber = 4000000

totalSum = 2
lastNum = 2
nextNum = 3
while nextNum <= maxNumber:
    if nextNum%2==0:
        totalSum += nextNum

    tmp = lastNum + nextNum
    lastNum = nextNum
    nextNum = tmp
    print nextNum

print 'Sum of all even fibonacci numbers below',maxNumber,':',totalSum
