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

conwaysOneLine = lambda numSteps=GAMEITTER, state=INITSTATE:[(state := [[(1 if (state[i][j] == 1 and ((sum([state[(i + ([1,1,1,0,-1,-1,-1,0])[k]) % len(state)][(j + ([1,1,1,0,-1,-1,-1,0])[(k + 2) % 8]) % len(state[0])] for k in range(8)])) in [2,3]) or (state[i][j] == 0 and (sum([state[(i + ([1,1,1,0,-1,-1,-1,0])[k]) % len(state)][(j + ([1,1,1,0,-1,-1,-1,0])[(k + 2) % 8]) % len(state[0])] for k in range(8)])) == 3)) else 0) for j in range(GAMESIZE[1])] for i in range(GAMESIZE[0])]) for step in range(numSteps)]

plt.rcParams['animation.convert_path'] = "C:/msys64/mingw64/bin/magick.exe"
fig = plt.figure()
ims = [[plt.imshow(state, interpolation='nearest')] for state in conwaysOneLine()]
animation.ArtistAnimation(fig, ims, interval=50, blit=False, repeat_delay=500).save("conways.gif", writer="imagemagick")