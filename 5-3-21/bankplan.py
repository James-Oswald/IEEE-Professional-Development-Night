#https://www.codewars.com/kata/56445c4755d0e45b8c00010a


def fortune(f0, p, c0, n, i):
    print(str(f0) + " " + str(c0) + " " + str(n))
    if n == 1:
        return f0 >= 0
    else:
        f0 = int(f0)
        c0 = int(c0)
        f1 = int(f0 + (p/100) * f0 - c0)
        c1 = int(c0 + c0*(i/100))
        return fortune(f1, p, c1, n-1, i)
    

print(fortune(100000, 1, 2000, 15, 1)) # True
print(fortune(100000, 1, 10000, 10, 1)) # True
print(fortune(100000, 1, 9185, 12, 1)) # False