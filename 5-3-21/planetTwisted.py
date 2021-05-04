#https://www.codewars.com/kata/58068479c27998b11900056e


def twistedSort(arr):
    rv = arr.copy()
    rv.sort(key=lambda e:int(str(e).replace("3", "x").replace("7", "3").replace("x", "7")))
    return rv

print(twistedSort([1,2,3,4,5,6,7,8,9])) #[1,2,7,4,5,6,3,8,9]
print(twistedSort([12,13,14])) #[12,14,13]
print(twistedSort([9,2,4,7,3])) #[2,7,4,3,9]