

#https://www.codewars.com/kata/5679aa472b8f57fb8c000047

#O(n^2) 
#python sum returns 0 for empty arrays, sum([]) == 0
def eqSidesBad(arr):
    for index in range(0, len(arr)):
        if sum(arr[:index]) == sum(arr[index+1:]):
            return index
    return -1

#O(2n)
def eqSidesGood(arr):
    right = sum(arr)
    left = 0
    for index in range(0, len(arr)):
        if left == right - arr[index]:
            return index
        right -= arr[index]
        left += arr[index]
    return -1

eqSides=lambda a,r=0:r[0]if(r:=[i for i in range(len(a))if sum(a[:i])==sum(a[i+1:])])else-1

print(eqSides([1,2,3,4,3,2,1])) #3
print(eqSides([1,100,50,-51,1,1])) #1
print(eqSides([20,10,-80,10,10,15,35])) #0
print(eqSides([1,2,3,4,5,6])) #-1