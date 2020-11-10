
import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.animation as animation

GAMEITTER = 30
GAMESIZE = (100, 100)
(INITSTATE := np.zeros(GAMESIZE))[int(GAMESIZE[0]/2):int(GAMESIZE[0]/2 + 3), int(GAMESIZE[1]/2):int(GAMESIZE[1]/2 + 7)] = [
[1, 1, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0]]

def conwaysSmaller(numSteps=GAMEITTER, state=INITSTATE):
    arround = [1,1,1,0,-1,-1,-1,0]
    numNeibors = lambda i,j: sum([state[(i + arround[k]) % len(state)][(j + arround[(k + 2) % 8]) % len(state[0])] for k in range(8)])
    cellLogic = lambda nn, i, j: 1 if (state[i][j] == 1 and (nn in [2,3]) or (state[i][j] == 0 and nn == 3)) else 0
    return [(state := [[cellLogic(numNeibors(i,j), i, j) for j in range(GAMESIZE[1])] for i in range(GAMESIZE[0])]) for step in range(numSteps)]

plt.rcParams['animation.convert_path'] = "C:/msys64/mingw64/bin/magick.exe"
fig = plt.figure()
ims = [[plt.imshow(state, interpolation='nearest')] for state in conwaysSmaller()]
animation.ArtistAnimation(fig, ims, interval=50, blit=False, repeat_delay=500).save("conways.gif", writer="imagemagick")