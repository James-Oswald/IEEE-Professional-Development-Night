

def parOut(arr):
    count = 0
    for i in range(3):
        count += 1 if arr[i] % 2 != 0 else -1
    parity = 1 if count > 0 else 0
    for elm in arr:
        if elm % 2 + parity != 0:
            return elm

print(parOut([2, 4, 0, 100, 4, 11, 2602, 36]))
print(parOut([160, 3, 1719, 19, 11, 13, -21]))