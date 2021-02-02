# https://www.codewars.com/kata/523f5d21c841566fde000009

def arrayDif(a1, a2):
    rv = a1.copy()
    for val in a2:
        while(rv.count(val)): 
            rv.remove(val)
    return rv

print(arrayDif([1,2],[1])) # [2]
print(arrayDif([1,2,2,2,3], [2])) # [1,3]