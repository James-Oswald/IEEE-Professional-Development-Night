
#This implmentation is incomplete and broken

import numpy as np
from matplotlib import pyplot as plt
boardSize = (20, 20)
itterations = 20
boardState = np.zeros(boardSize)
acorn = [
[1, 1, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0]]
boardState[10:13,8:15] = acorn
for itter in range(0, itterations):
    newState = np.zeros(boardSize)
    for i in range(0, len(boardState)):
        for j in range(0, len(boardState[0])):
            hell = [1,1,1,0,-1,-1,-1,0]
            nextTo = 0
            for k in range(0, 8):
                if(boardState[(i + hell[k]) % len(boardState), (j + hell[(k + 2) % 8]) % len(boardState[0])] == 1):
                    nextTo = nextTo + 1
            if boardState[i, j] == 1 and (nextTo == 2 or nextTo == 3):
                newState[i, j] = 1  
            elif boardState[i, j] == 0 and nextTo == 3:
                newState[i, j] = 1
            else:
                newState[i, j] = 0
    plt.imshow(newState, interpolation='nearest')
    print(newState)
    plt.show()
    boardState = np.copy(newState)
    #print("=========\n")
    print(boardState)
    #plt.imshow(boardState, interpolation='nearest')
    #plt.show()
