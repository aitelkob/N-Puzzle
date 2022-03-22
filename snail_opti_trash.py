def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]
def snail(map2d):
    length = len(map2d)
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
    lst = convert_1d_to_2d(lst,length)
    return lst

