

#https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sortOdd(arr):
    oddPositions = []
    oddNumbers = []
    returnArr = arr.copy()
    for i in range(len(arr)):                       #Store positions and odds
        if arr[i] % 2 == 1:
            oddPositions.append(i)
            oddNumbers.append(arr[i])
    oddNumbers.sort()                               #sort odds
    for i in range(len(oddPositions)):              #reinsert odds
        returnArr[oddPositions[i]] = oddNumbers[i]
    return returnArr

print(sortOdd([7, 1])) #[1, 7]
print(sortOdd([5, 8, 6, 3, 4])) #[3, 8, 6, 5, 4]
print(sortOdd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) #[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]