def Puzzle_goal(size):
    puzzle = []
    for number in range(0, size):
        puzzle.append([0] * size)
    
    i, j = 0, 0
    number = 0
    xsize = size - 1
    ysize = size - 1
    magic = 0
    while magic < size:
        i = magic
        j = magic
        while j <= ysize - magic:
            puzzle[i][j] = number + 1
            number += 1
            j += 1
        i += 1
        j -= 1
        while i <= xsize - magic:
            puzzle[i][j] = number + 1
            number += 1
            i += 1
        j -= 1
        i -= 1
        while j >= magic:
            puzzle[i][j] = number + 1
            number += 1
            j -= 1
        j += 1
        i -= 1
        while i > magic:
            puzzle[i][j] = number + 1
            number += 1
            i -= 1
        magic += 1
    
    i, j = 0, 0
    while i < size:
        j = 0
        while j < size:
            if puzzle[i][j] == (size * size):
                puzzle[i][j] = 0
            j += 1
        i += 1
    return puzzle
