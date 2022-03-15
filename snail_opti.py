def snail(map2d):
    lst = []
    while len(map2d) != 0:
        lst.extend(map2d[0])
        map2d.remove(map2d[0])
        if len(map2d) == 0:
            break
        for i in map2d:
            lst.append(i.pop())
        lst.extend(reversed(map2d[len(map2d)-1]))
        map2d.remove(map2d[len(map2d)-1])
        if len(map2d) != 1:
            list2 = []
            for i in map2d:
                list2.append(i.pop(0))
            lst.extend(reversed(list2))
    return lst
array2 = [[1,2,3],
         [4,5,6],
         [7,8,9]]
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]
print("result",snail(array))
