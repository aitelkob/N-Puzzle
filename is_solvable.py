from turtle import goto


def solve_or_nop(arr):
    arr = [j for sub in arr for j in sub]
    cpt = 0
    empty = -1
    for i in range(0,9):
        for j in range(i + 1,9):
            if arr[j] != empty and arr[i] != empty and arr[i] > arr[j]:
                cpt+=1
    if cpt %2 == 0:
        print(cpt)
        return "solve"
    else:
        print(cpt)
        return "nop"

###### test how many inversion in map 
arr = [[8, 1, 2],[4, 0, 3],[6, 7, 5]]
goal_puzzle = [[1,2,3],[8,0 , 4],[7, 6, 5]]
puzzle = [[8, 1, 2],[-1, 4, 3],[7, 6, 5]]
print(solve_or_nop(arr))