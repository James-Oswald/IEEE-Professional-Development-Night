#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def printSubArrays(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array) + 1):
            print(array[i:j])

# Solutions to the problem

#O(n^3)
def maxSubarraysum(array):
    maxSum = 0
    for i in range(0, len(array)):
        for j in range(i + 1, len(array) + 1):
            currentSum = sum(array[i:j])
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum

#O(n)
def maxSubarraysumFast(array):
    add = 0; maximum = 0
    for val in array:
        add = max(0, add + val)
        maximum = max(maximum, add)
    return maximum

#The following work even without the "If the list is made up of only negative numbers, return 0 instead." constraint

#O(n^3)
def maxSubarraysumNeg(array):
    maxSum = array[0]
    for i in range(0, len(array)):
        for j in range(i + 1, len(array) + 1):
            currentSum = sum(array[i:j])
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum

#O(n)
def maxSubarraysumFastNeg(array):
    add = 0; maximum = 0; posFlag = False
    for val in array:
        if val > 0:
            posFlag = True
        add = max(0, add + val)
        maximum = max(maximum, add)
    return maximum if posFlag else max(array)

#printSubArrays([-2, 1, -3, 4, -1, 2, 1, -5, 4])
arr2 = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
print(maxSubarraysum(arr2))
print(maxSubarraysumFast(arr2))



            