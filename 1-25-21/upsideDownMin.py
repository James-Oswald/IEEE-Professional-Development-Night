

opp = {"0" : "0", "1" : "1", "2" : None, "3" : None, "4" : None, "5" : None, "6" : "9", "7" : None, "8" : "8", "9" : "6"}

def isUpsidedown(num):
    num = str(num)
    if len(num) % 2 != 0:
        center = len(num) // 2
        if opp[num[center]] != num[center]:
            return False
    for index in range(len(num) // 2):
        if opp[num[index]] == None or num[index] != opp[num[-(index + 1)]]:
            return False 
    return True

#def isUpsidedownMin(num):
#    len(num) % 2 != 0 
#    sum([int(opp[str(num)[index]] == None or str(num)[index] != opp[str(num)[-(index + 1)]]) for index in range(len(str(num)) // 2)])

print(isUpsidedown("6969"))
print(isUpsidedown("9116"))
print(isUpsidedown("8"))
print(isUpsidedown("2222"))