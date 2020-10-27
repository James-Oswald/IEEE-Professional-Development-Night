#https://www.codewars.com/kata/59f11118a5e129e591000134

def repeats(array):
    return sum([i for i in array if array.count(i) == 1])

print(repeats([4,5,7,5,4,8]))