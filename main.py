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
    print("-->", regexString)
    for item in map:
        if re.search(regexString, item) is None:
            print("item :", item)
            return False
    return True

with open(arv) as file:
    string = file.read()
    data = string.split("\n")
    cleanData = clearComments(data)
    length = int(cleanData[0])
    if mapChecker(cleanData, length) is False:
        print("the map you introduced is invalid")


print(data)
print(cleanData)