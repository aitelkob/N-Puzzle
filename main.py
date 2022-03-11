import sys


arv = sys.argv[1]
len = 0
map = []

with open(arv) as file:
    string = file.read()
    data = string.split("\n")
    len = data[1]
    
    # cleanData = []
    # for item in data:
    #     if item.startswith("#"):
    #         continue
    #     else

print(data)