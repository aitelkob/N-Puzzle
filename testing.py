directions = [
    lambda i, j: (i, j + 1),
    lambda i, j: (i + 1, j),
    lambda i, j: (i, j - 1),
    lambda i, j: (i - 1, j),
]

array = [[1,2,3,4],
         [4,5,6,7],
         [8,9,10,11],
         [12,13,14,15]]

def in_matrix(i, j):
    return 0 <= i < len(array) and 0 <= j < len(array)

def is_visited(i, j):
    return array[i][j] == 0


def snail(array):
    direction_cnt = 0
    i, j = 0, 0
    ret = []
    ret.append(array[i][j])
    array[i][j] = 0  # mark as visited
    while True:
        direction_func = directions[direction_cnt % 4]  # turning directions in circle
        tmp_i, tmp_j = direction_func(i, j)  # attempt to head one step
        if (not in_matrix(tmp_i, tmp_j)) or is_visited(tmp_i, tmp_j):  # over border or visted
            direction_cnt += 1  # change direction
        else:
            i, j = tmp_i, tmp_j  # confirm this step
            ret.append(array[i][j])
            array[i][j] = 0  # mark as visited
            if len(ret) == len(array)**2:  # simple terminal criteria
                return ret


if __name__ == '__main__':
    print snail(array)

