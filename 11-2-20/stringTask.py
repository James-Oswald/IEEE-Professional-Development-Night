#https://www.codewars.com/kata/598ab63c7367483c890000f4

def strTaskMax(string):
    newStr = ""
    for letter in string.lower():
        if(letter in ['a', 'e', 'i', 'o', 'u', 'y']):
            continue
        newStr += "." + letter
    return newStr

strTask = lambda s: ''.join(['.' + l for l in s.lower() if l not in ['a', 'e', 'i', 'o', 'u', 'y']])


print(strTask('tour'))
print(strTask('Codewars'))
print(strTask('aBAcAba'))