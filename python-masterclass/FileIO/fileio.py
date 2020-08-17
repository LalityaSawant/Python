# filecontent = open("/Users/lalityasawant/Documents/Programming/Python/python-masterclass/FileIO/original.txt","r")

# filecontent = open("original.txt","r")
#
# for line in filecontent:
#     if "with" in line.lower():
#         print(line, end="")
#
# filecontent.close()


#no need to use close with "with open"
# with open("original.txt","r") as filecontent:
#     for line in filecontent:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("original.txt","r") as filecontent:
#     line = filecontent.readline()
#     while line:
#         print(line, end='')
#         line = filecontent.readline()

# with open("original.txt","r") as filecontent:
#     lines = filecontent.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

with open("original.txt","r") as filecontent:
    lines = filecontent.read()

for line in lines:
    print(line, end="")

