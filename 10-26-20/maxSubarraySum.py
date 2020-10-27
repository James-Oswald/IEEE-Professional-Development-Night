#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def maxSubarraysum(array):
    maxSum = 0
    for i in range(0, len(array)):
        for j in range(i + 1, len(array) + 1):
            currentSum = sum(array[i:j])
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum


def printSubArrays(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array) + 1):
            print(array[i:j])

printSubArrays([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(maxSubarraysum([]))
print(maxSubarraysum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



            