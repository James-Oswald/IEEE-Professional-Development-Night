
#https://www.codewars.com/kata/525f50e3b73515a6db000b83

def createPhoneNumber(nums):
    charNums = [str(num) for num in nums]
    return "("+"".join(charNums[:3])+") "+"".join(charNums[3:6])+"-"+"".join(charNums[6:])

def createPhoneNumberMin(n):
    c = [str(m) for m in n]; 
    return "("+"".join(c[:3])+") "+"".join(c[3:6])+"-"+"".join(c[6:])

createPhoneNumber=lambda n,s=str:"("+s(n[0])+s(n[1])+s(n[2])+") "+s(n[3])+s(n[4])+s(n[5])+"-"+s(n[6])+s(n[7])+s(n[8])+s(n[9])
#createPhoneNumber=lambda n,r=0,f=0,s=str:r if (f=lambda x:s(n[x]))and(r:="("+f(0)+f(1)+f(2)+") ")else-1

print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) #"(123) 456-7890"
