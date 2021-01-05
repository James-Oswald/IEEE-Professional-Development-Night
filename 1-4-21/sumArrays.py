#https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

def addArrays(arr1, arr2):
    n1 = int("".join(map(str, arr1)))
    n2 = int("".join(map(str, arr2)))
    rv = str(n1 + n2)
    if rv[0] == "-":
        rv = [int(char) for char in rv[1:]]
        rv[0] = -rv[0]
        return rv
    else:
        return [int(char) for char in rv]

#addArraysL = lambda a1, a2, rv=0: [int(char) for char in str]

print(addArrays([3,2,9],[1,2]))
print(addArrays([4,7,3],[1,2,3]))
print(addArrays([1],[5,7,6]))
print(addArrays([3,2,6,6],[-7,2,2,8]))