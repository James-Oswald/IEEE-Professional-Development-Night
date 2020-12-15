
gps = lambda x, s: int(max([3600 * abs(x[i] - x[i+1]) / s for i in range(len(x) - 1)])) if len(x) > 1 else 0

print(gps([0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25], 15))