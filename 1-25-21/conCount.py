#https://www.codewars.com/kata/59c3e819d751df54e9000098

def conCount(items, key):
    items = str(items)
    key = str(key)
    acc = 0
    maxAcc = 0
    for item in items:
        if item == key:
            acc += 1
            if acc > maxAcc:
                maxAcc = acc
        else:
            acc = 0
    return maxAcc

print(conCount(90000, 0))           #-->  4
print(conCount("abcdaaadse", "a"))   # -->  3
print(conCount("abcdaaadse", "z"))   #-->  0