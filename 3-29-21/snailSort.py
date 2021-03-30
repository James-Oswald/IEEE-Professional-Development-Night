
#https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

def snailSort(matrix):
    n = len(matrix)
    visited = [[0] * n] * n
    directionsX = [1, 0, -1, 0]
    directionsY = [0, -1, 0, 1]
    directionIndex = 0
    x = 0
    y = 0
    outputArray = []
    canMove = True
    while canMove:
        outputArray.append(matrix[x][y])
        visited[x][y] = 1
        nextX = x + directionsX[directionIndex]
        nextY = y + directionsY[directionIndex]
        if nextX >= n or nextY >= n or visited[nextX][nextY] == 1:
            directionIndex += 1
            
            nextX = x + directionsX[directionIndex]
            nextY = y + directionsY[directionIndex]
        if nextX >= n or nextY >= n or visited[nextX][nextY] == 1:
            canMove = False
        x = nextX
        y = nextY
    return outputArray

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snailSort(array))