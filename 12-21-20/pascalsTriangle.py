
#https://www.codewars.com/kata/5226eb40316b56c8d500030f

def pascalM(n):
    rv = [1]
    row = [1]
    for i in range(n - 1):
        row = [1] + [row[j] + row[j+1] for j in range(i)] + [1]
        rv += row
    return rv

def pascal(n):
    rv = [1]
    row = [1]
    for i in range(n - 1):
        row2 = []
        for j in range(i): 
            row2.append(row[j] + row[j+1])
        row = [1] + row2 + [1]
        rv += row
    return rv
    
print(pascal(1))
print(pascal(2))
print(pascal(3))
print(pascal(4))