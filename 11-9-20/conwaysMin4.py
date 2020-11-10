import numpy as np
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
import matplotlib.animation as animation

G = 30
S = (100, 100)
(I := np.zeros(S))[int(S[0]/2):int(S[0]/2 + 3), int(S[1]/2):int(S[1]/2 + 7)] = [
[1, 1, 0, 0, 1, 1, 1],
[0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0]]

def cgol(g=G, s=I):
    a=[1,1,1,0,-1,-1,-1,0]
    n=lambda i,j: sum([s[(i+a[k])%len(s)][(j+a[(k+2)%8])%len(s[0])] for k in range(8)])
    c=lambda m,i,j:1 if (s[i][j]==1 and (m in [2,3]) or (s[i][j]==0 and m==3)) else 0
    return [(s:=[[c(n(i,j),i,j) for j in range(S[1])] for i in range(S[0])]) for step in range(g)]

plt.rcParams['animation.convert_path'] = "C:/msys64/mingw64/bin/magick.exe"
fig = plt.figure()
ims = [[plt.imshow(state, interpolation='nearest')] for state in cgol()]
animation.ArtistAnimation(fig, ims, interval=50, blit=False, repeat_delay=500).save("conways.gif", writer="imagemagick")