
#This question was provided to us from one of our members
#https://cdn.discordapp.com/attachments/795816943344680982/800891961275449364/Screen_Shot_2021-01-12_at_5.png

def decodeNumbers(inp):
    if len(inp) == 0:
        return 1
    if len(inp) == 1:
        return 1 if int(inp[0]) != 0 else 0
    acc = 0
    if len(inp) >= 2 and int(inp[0:2]) <= 26:
        acc += decodeNumbers(inp[2:])
    if len(inp) >= 1 and int(inp[1]) != 0:
        acc += decodeNumbers(inp[1:])
    return acc

print(decodeNumbers("2")) #2    | 1 2 or 12
print(decodeNumbers("123")) #3   | 1 2 3 or 12 3 or 1 23
print(decodeNumbers("127")) #2   | 1 2 7 or 12 7
print(decodeNumbers("1028")) #1  | 10 2 8
print(decodeNumbers("101010")) #1 
print(decodeNumbers("2016")) #2  | 20 16 or 20 1 6 
print(decodeNumbers("1212")) #5  | 1 2 1 2 or 12 12 or 1 21 2 or 1 2 12 or 12 1 2 
print(decodeNumbers("1210")) #2  | 1 2 10 or 12 10 
print(decodeNumbers("100")) #0 
print(decodeNumbers("0")) #0 
print(decodeNumbers("000")) #0