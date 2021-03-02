
#https://www.codewars.com/kata/5552101f47fc5178b1000050

def digiPow(theNumber, basePower):
    digitArray = []                             #Turn our number into an array of digits
    for digit in str(theNumber):
        digitArray.append(int(digit))
    theSum = 0                                  #sum up each digit with exponent
    theExponent = basePower
    for i in range(len(digitArray)):
        theSum += digitArray[i]**theExponent
        theExponent += 1
    if theSum % theNumber != 0:                 #check if its divisable by the number and return k
        return -1
    else:
        return int(theSum / theNumber)

print(digiPow(89, 1))   # 1
print(digiPow(92, 1))   # -1
print(digiPow(695, 2))  # 2
print(digiPow(46288, 3))# 51