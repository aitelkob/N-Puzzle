from re import S
import re
import sys


arv = sys.argv[1]
length = 0
map = []

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

with open(arv) as file:
    string = file.read()
    data = string.split("\n")
    cleanData = clearComments(data)
    length = int(cleanData[0])
    result = mapChecker(cleanData, length)
    if result[0] is False:
        print("the map you introduced is invalid")
    else:
        map = result[1]

def checkMapIsValid(map, length):
    values = list(range(0, length * length))
    allItems = []
    spliteLine = []
    for item in map:
        spliteLine = item.split(' ')
        for each in spliteLine:
            allItems.append(int(each))
    # for number in values:
    #     if number not in allItems:
    #         print("dkllsgl")
    allItems.sort()
    if (allItems == values):
        print(values)
            

checkMapIsValid(map, length)
print(map, length)
