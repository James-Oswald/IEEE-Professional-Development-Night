
#fat recursive
def triangularMax(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    return n + triangularMax(n - 1)

#minimal recursive
triangularM = lambda n: (n + triangular(n - 1) if n > 1 else 1) if n > 0 else 0

#omega small
triangular = lambda n: sum(range(0, n)) if n > 0 else 0

for i in range(-1, 5):
    print("triangular(" + str(i) + "):" + str(triangular(i)))