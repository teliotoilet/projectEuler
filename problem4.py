#!/usr/local/bin/python

def checkPalindrome(digits):
    ncheck = len(digits)/2
    return all([digits[i]==digits[-i-1] for i in range(ncheck+1)])

# brute force way...

foundPalindromes = []
for num1 in range(100,1000):
#    for num2 in range(num1,1000):
# this is faster:
    for num2 in range(num1,1000):

# This doesn't find the largest palindrome!
#found = False
#for num1 in range(999,99,-1):
#    for num2 in range(999,99,-1):
        prod = num1*num2
        order = 10
        digits = [prod%order]
        curValue = digits[-1]
        while order < prod:
            lastOrder = order
            order *= 10
            lastValue = curValue
            curValue = prod%order
            digits.append( (curValue-lastValue)/lastOrder )
        if checkPalindrome(digits):
            print num1,num2,prod
            foundPalindromes.append(prod)
#            found = True
#            break
#    if found:
#        break
        
print max(foundPalindromes)
