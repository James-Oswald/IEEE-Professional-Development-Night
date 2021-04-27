#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08

import numpy as np

def mult(num):
    mat = np.repeat(np.expand_dims(np.arange(1, num + 1), 1), num, axis=1)
    return np.multiply(np.transpose(mat), mat)

print(mult(5))