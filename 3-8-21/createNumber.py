
#https://www.codewars.com/kata/525f50e3b73515a6db000b83

def createPhoneNumber(nums):
    charNums = [str(num) for num in nums]
    return "("+"".join(charNums[:3])+") "+"".join(charNums[3:6])+"-"+"".join(charNums[6:])

#createPhoneNumber = lambda n,j=(lambda m,x,y:"".join()):""%

print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #"(123) 456-7890"
