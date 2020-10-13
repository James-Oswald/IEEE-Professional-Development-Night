
#https://www.codewars.com/kata/5a3e1319b6486ac96f000049

def countSubsequentPairs(array):
    count = 0
    for i in range(0, len(array) - 1, 2):
        if abs(array[i] - array[i+1]) == 1:
            count = count + 1
    return count

arr = [1, 2, 5, 8, -4, -3, 7, 6, 5]
print(countSubsequentPairs(arr))