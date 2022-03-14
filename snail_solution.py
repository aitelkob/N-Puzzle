RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
NB_DRIECTIONS = 4

def next_direction(direction):
    return (direction +1) % NB_DRIECTIONS
def update_position(position,direction):
    x,y = position
    if direction == RIGHT:
        return x+1,y
    elif direction == DOWN:
        return x,y+1
    elif direction == LEFT:
        return x-1,y
    elif direction == UP:
        return x,y-1
def get_value(arr,position):
    x,y = position
    return arr[x][y]
def set_as_visited(arr, position):
    x,y = position
    arr[x][y] = '*'
def is_visoted(arr, position):
    return get_value(arr,position) == '*'
def snail_arr(array):
    # compute the array size
    array_size = len(array) * len(array[0])

    # surround the array of '*'
    array = [['*' for _ in range(len(array[0]) + 2)]] + [
        ['*'] + array[i] + ['*']
        for i in range(len(array))
    ] + [['*' for _ in range(len(array[0]) + 2)]]

    # initialize position and direction
    position = 1, 1
    direction = RIGHT

    result = [get_value(array, position)]
    set_as_visited(array, position)
    nb_visited = 1

    while nb_visited < array_size:
        new_position = update_position(position, direction)
        if not is_visoted(array, new_position):
            result += [get_value(array, new_position)]
            set_as_visited(array, new_position)
            position = new_position
            nb_visited += 1
        else:
            direction = next_direction(direction)
    return result

array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(array)
print(snail_arr(array))

