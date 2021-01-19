#https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/java

def validPhoneNumber(phoneNumber):
    frmt = "(nnn) nnn-nnnn"
    if len(frmt) != len(phoneNumber):
        return False
    for i in range(len(phoneNumber)):
        number = (frmt[i] == "n" and ord(phoneNumber[i]) >= ord("0") and ord(phoneNumber[i]) <= ord("9"))
        symbol = frmt[i] == phoneNumber[i]
        if not (number or symbol):
            return False
    return True
        

print(validPhoneNumber("(123) 456-7890"))
print(validPhoneNumber("(1111)555 2345"))
print(validPhoneNumber("(098) 123 4567"))