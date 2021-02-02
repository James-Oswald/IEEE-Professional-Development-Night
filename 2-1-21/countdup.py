#https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def countDup(string):
    charDict = {}
    string = string.lower()
    for char in string:
        if char not in charDict.keys():
            charDict[char] = 0
        else:
            charDict[char] += 1
    acc = 0
    for key in charDict.keys():
        if charDict[key] > 0:
            acc += 1
    return acc

print(countDup("abcde")) #0
print(countDup("aabbcde")) #2
print(countDup("aabBcde")) #2
print(countDup("indivisibility")) #1
print(countDup("Indivisibilities")) #2
print(countDup("aA11")) #2
print(countDup("ABBA")) #2
