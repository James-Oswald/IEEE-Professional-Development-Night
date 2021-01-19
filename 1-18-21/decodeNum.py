



def decodeNumbers(inp):
    if len(inp) == 1:
        return 1
    acc = 0
    if len(inp) > 2 and int(inp[0:2]) <= 26:
        acc += decodeNumbers(inp[2:])
    acc += decodeNumbers(inp[1:])
    return acc

print(decodeNumbers("12")) #2 |  1 2 or 12
print(decodeNumbers("123")) #3   | 1 2 3 or 12 3 or 1 23
print(decodeNumbers("127")) #2   | 1 2 7 or 12 7