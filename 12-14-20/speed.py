
import math

def gps(x, s):
    ahs = []
    for i in range(len(x) - 1):
        deltaDistance = abs(x[i] - x[i + 1])
        ahs.append(3600 * deltaDistance / s)
    return math.floor(max(ahs))

print(gps([0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25], 15))