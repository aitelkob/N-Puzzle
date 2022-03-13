RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
NB_DRIECTIONS = 4

def next_direction(direaction):
    return (direction +1) % NB_DRIECTIONS
def update_postion(position,direction):
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

def snail_arr(arr):
    # get size of arr 
    arr_len = len(arr) * 2
    arr_len2  = len(arr) * len(arr[0])
    print(arr_len,arr_len2)
    array = [['*' for _ in range(len(arr[0]) + 2)]] + [
        ['*'] + arr[i] + ['*']
        for i in range(len(arr))
    ] + [['*' for _ in range(len(arr[0]) + 2)]]


array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
snail_arr(array)

