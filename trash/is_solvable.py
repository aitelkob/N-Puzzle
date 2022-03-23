
def solve_or_nop(arr, size):
    arr = [j for sub in arr for j in sub]
    cpt = 0
    empty = -1
    for i in range(0,size):
        for j in range(i + 1,size):
            if arr[j] != empty and arr[i] != empty and arr[i] > arr[j]:
                cpt+=1
    if cpt %2 == 0:
        print(cpt)
        return True
    else:
        print(cpt)
    return False
#### outman way but better 
def trash_improved(arr,solved,size):
    res = 0
    cpt = 0
    for i in range(size ):
        for j in range(size):
            var1 = arr[i][j]
            var2 = solved[j][j]
            print(var1,var2)
            if  solved.index(var1) > solved.index(var2):
                cpt+=1
    return cpt

# ###### test how many inversion in map 
# arr = [[8, 1, 2],[4, 0, 3],[6, 7, 5]]
# goal_puzzle = [[1,2,3],[8,0 , 4],[7, 6, 5]]
# puzzle = [[8, 1, 2],[-1, 4, 3],[7, 6, 5]]
# print(solve_or_nop(arr))
# print(len(arr[0]))
# print(trash_improved(arr,goal_puzzle, 3 ))