
upsideDown = {"0" : "0", "1" : "1", "2" : None, "3" : None,
             "4" : None, "5" : None, "6" : "9", "7" : None,
             "8" : "8", "9" : "6"}

def isUpsidedown(num):
    num = str(num)
    if len(num) == 0:
        return True
    if len(num) == 1:
        return upsideDown[num] == num
    if num[0] != upsideDown[num[len(num) - 1]]:
        return False
    return isUpsidedown(num[1:-1])



print(isUpsidedown("6969"))
print(isUpsidedown("9116"))
print(isUpsidedown("8"))
print(isUpsidedown("2222"))