
#https://www.codewars.com/kata/59b11f57f322e5da45000254

def onesComplementMax(string):
    rv = ""
    for char in string:
        if char == "0":
            rv += "1"
        elif char == "1":
            rv += "0"
    return rv

onesComplement = lambda string: "".join([["1", "0"][int(char)] for char in string])

print(onesComplement("1001"))
print(onesComplement("1010"))
