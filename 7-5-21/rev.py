#https://leetcode.com/problems/reverse-integer

def reverse(x: int) -> int:
    fullArr=list(str(x))
    digiArr=fullArr[1:]if fullArr[0]=="-"else fullArr
    digiArr.reverse()
    revVal = int("".join((["-"] + digiArr) if fullArr[0]=="-" else digiArr))
    if revVal < -2**31-1 or revVal > 2**31:
        return 0
    return revVal

print(reverse(-123))