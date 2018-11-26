## Input & Output ##

## Reading Files ##

# jabber = open("sample.txt",'r')
# # jabber = open("C:\\Documents and Settings\\tim\\My Documents\\sample.text",'r')       Windows Style
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end='')
#
# jabber.close()          # IMPORTANT, can corrupt file, can cause errors opening later as well

# with open("sample.txt",'r') as jabber:      # with closes file for us, ensures files are closed when errors happen
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt",'r') as jabber:
#     line = jabber.readline()        # if there is an issue, it won't get to the while loop stage
#     while line:                     # continues until no more lines to read
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("sample.txt",'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

with open("sample.txt",'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')


# read line reads a single line from a file and returns a string, read one line at a time, recommended approach
# read lines reads the entire file and returns a list of strings, can cause memory problems
# read, reads the entire file and if it's a text file returns a string containing the contents of the file