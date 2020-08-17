parrot = "Norwegian Blue"

for character in parrot:
    print(character)

#number = "9,223;372:036 854,775;907"
number = input("Please enter a series of numbers, using any separators: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


