
import math

isPrime = lambda n: True not in [n % i == 0 for i in range(2, int(math.sqrt(n)) + 1)]

def minimumNumber(numList):
    minNumber = 0
    while not isPrime(sum(numList) + minNumber):
        minNumber += 1
    return minNumber

print(minimumNumber([3,1,2]))
print(minimumNumber([2,12,8,4,6]))
print(minimumNumber([50,39,49,6,17,28]))