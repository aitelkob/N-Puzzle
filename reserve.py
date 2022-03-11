from itertools import count
import sys
import re 

#(?m) enables the multiline mode. ^ asserts that we are at the start. <space>*# matches the character 
# at the start with or without preceding spaces. .* matches all the following characters except line breaks. 
# Replacing those matched characters with empty string will give you the string with comment lines deleted.
def stripComments(code):
    return re.sub(r'(?m) *#.*\n?', '\n', code)

arv = sys.argv[1]
length = 0
map = []

with open(arv) as file:
    string = file.read()
    # first i need to remove #comment
    clean_comment = stripComments(string)
    clean_space = clean_comment.split("\n")
    # secound remove empty lines
    data = [index for index in clean_space if index]
    # check regex of map
    length = int(data.pop(0))
    # take length of map 
    # map = data

# print("this is length of the puzzle  = ",length)
# print(str_regex)