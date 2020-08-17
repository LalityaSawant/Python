day = 'Saturday'
temperature = 30
raining = True

if day == 'Saturday' and temperature > 27 and not raining:
    print('Go Swimming')
else:
    print('Learn Python')


print('-' * 30)

if (day == 'Saturday' and temperature > 27) or not raining:
    print('Go Swimming')
else:
    print('Learn Python')

print('-' * 50)

if 0:
    print('True')
else:
    print('False')

name = input("Enter name: ")
#if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name")
