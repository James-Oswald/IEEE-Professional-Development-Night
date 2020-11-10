
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.animation as animation

plt.rcParams['animation.convert_path'] = "C:/msys64/mingw64/bin/magick.exe"
fig = plt.figure()

boardSize = (30, 30)
itterations = 30
boardState = np.zeros(boardSize)
ims = []
acorn = [
[1, 1, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0]]
boardState[int(boardSize[0]/2):int(boardSize[0]/2 + 3), int(boardSize[1]/2):int(boardSize[1]/2 + 7)] = acorn
for itter in range(0, itterations):
    print("Generating Step #" + str(itter))
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
    ims.append([plt.imshow(newState, interpolation='nearest')])
    boardState = np.copy(newState)
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=False, repeat_delay=500)
ani.save("conways.gif", writer="imagemagick")
