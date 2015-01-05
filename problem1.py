#!/usr/local/bin/python

maxNumber = 1000
multiplesOf = [3,5]

totalSum = 0
for num in range(maxNumber):
    if any([num%val==0 for val in multiplesOf]):
        totalSum += num

print 'Sum of all multiples of',multiplesOf,'below',maxNumber,':',totalSum
