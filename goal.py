import numpy as np


def final_goal(size):
    direction = 0 
    i = 0
    j = 0
    out = np.zeros((size, size), dtype=int)
    for k in range(1,size * size):
        out[i][j] = k
        if direction == 0 and (j == size - 1 or out[i][j + 1] > 0):
            direction = 1
            i += 1
        elif direction == 0:
            j += 1
        elif direction == 1 and (i == size - 1 or out[i + 1][j] > 0):
            direction = 2
            j -= 1
        elif direction == 1:
            i += 1
        elif direction == 2 and (j == 0 or out[i][j - 1] > 0):
            direction = 3
            i -= 1
        elif direction == 2:
            j -= 1
        elif direction == 3 and (i == 0 or out[i - 1][j] > 0):
            direction = 0
            j += 1
        elif direction == 3:
            i -= 1
    return out
