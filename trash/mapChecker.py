import re
import sys

def clearComments(data):
    commentStart = 0
    cleanData = []
    for item in data:
        if item.find("#") != -1:
            commentStart = item.find("#")
            string = item[:commentStart]
            if string != '':
                cleanData.append(string)
        else:
            cleanData.append(item)
    return cleanData

def mapChecker(data, length):
    map = data[1:]
    regexString = '\d+\s' * length
    regexString = regexString[:-2]
    for item in map:
        if re.search(regexString, item) is None:
            return False, None
    return True, map

def getData(arv):
    with open(arv) as file:
        string = file.read()
        data = string.split("\n")
        cleanData = clearComments(data)
        try:
            length = int(cleanData[0])
        except TypeError:
            print("the map you introduced is invalid")
            sys.exit(1)
        result = mapChecker(cleanData, length)
        if result[0] is False:
            print("the map you introduced is invalid")
        else:
            map = result[1]
    return [length, map]
