
#https://www.codewars.com/kata/515f51d438015969f7000013/train/python


def pyramid(n):
    if n == 0:  #default case
        return []
    else:       #recursive case
        rv = pyramid(n-1)
        rv.append([1]*n)
        return rv

def pyramid1(n):
    rv = []
    for i in range(1, n+1):
        rv.append([1]*i)
    return rv

print(pyramid(0)) #=> [ ]
print(pyramid(1)) #=> [ [1] ]
print(pyramid(2)) #=> [ [1], [1, 1] ]
print(pyramid(3)) #=> [ [1], [1, 1], [1, 1, 1] ]