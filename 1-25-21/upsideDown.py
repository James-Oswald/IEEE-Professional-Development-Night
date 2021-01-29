
#codewars.com/kata/59f7597716049833200001eb

opp = {
    "0" : "0",
    "1" : "1",
    "2" : None,
    "3" : None,
    "4" : None,
    "5" : None,
    "6" : "9",
    "7" : None,
    "8" : "8",
    "9" : "6",
}

def isUpsidedown(num):
    num = str(num)
    if len(num) % 2 == 0:
        for index in range(len(num) // 2):
            if opp[num[index]] == None or num[index] != opp[num[-(index + 1)]]:
                return False 
        return True
    else:
        center = len(num) // 2
        if opp[num[center]] != num[center]:
            return False
        for index in range(len(num) // 2):
            if opp[num[index]] == None or num[index] != opp[num[-(index + 1)]]:
                return False 
        return True

def numUpsidedownInRange(start, stop):
    acc = 0
    for i in range(start, stop):
        if isUpsidedown(i):
            acc += 1
    return acc

print(isUpsidedown("6969"))
print(isUpsidedown("9116"))
print(isUpsidedown("8"))
print(isUpsidedown("2222"))
print(numUpsidedownInRange(0, 10)) #3
print(numUpsidedownInRange(10, 100)) #4
print(numUpsidedownInRange(100, 1000)) #12

