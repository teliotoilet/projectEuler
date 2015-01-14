#!/usr/local/bin/python
from mathTools import *

#startTriangleNumber = 3
#minDivisors = 5

startTriangleNumber = 10
#startTriangleNumber = 16570
minDivisors = 500


def triangleNum(ith,last=-1):
    if last < 0:
        return sum(range(1,ith+1))
    else:
        return last + ith

def factor(num,plist=[]):
    flist = [1]
    if num==1: return flist
#    orignum = num
#    flist += primefactor(num,plist)
#
#    # at this point, flist contains all _prime_ factors
#    print '  prime factors :',flist
#
#    nfac = len(flist)
#    while True:
#        for i in range(1,nfac): #skip flist[0], which is 1
#            for j in range(i+1,nfac):
#                newfac = flist[i]*flist[j]
#                if newfac <= orignum and orignum%newfac==0 and not newfac in flist:
#                    flist.append(newfac)
#        if len(flist) > nfac:
#            nfac = len(flist)
#        else:
#            break
    
    flist.append(num)
    for i in range(2,int(num**0.5)+2):
        if num%i==0:
            flist.append(i)
            if not i*i==num:
                flist.append(num/i)


    #flist.append(orignum)

    #print flist
    #return set(flist)

    #flist.sort()
    return flist

#------------------------------------------------------------------------------
    
#print triangleNum(7)

#for i in range(1,8):
#    num = triangleNum(i)
#    flist = factor(num)
#    print 'factors of',num,':',flist
#    print ''

itri = startTriangleNumber
num = triangleNum(itri)
flist = factor( num )
print 'triangle number',itri,'is',num, \
        'with',len(flist),'factors:', flist
while len(flist) <= minDivisors:
    itri += 1
    num = triangleNum(itri,num)

    #plist = primesLessThan(num)
    plist = primesLessThan(int(num**0.5)+1)
    #if len(plist) < minDivisors:
    #    print 'skipping triangle number',itri,'=',num
    #    continue

    flist = factor(num,plist)
    print 'triangle number',itri,'is',num, \
            'with',len(flist),'factors:', flist


