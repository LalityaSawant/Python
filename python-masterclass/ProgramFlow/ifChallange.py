name = input("Enter your name: ")

age = input("Enter your age: ")

if name != '' and age != '' and 18 <= int(age) < 31:
    print("Welcome to club 18-30 holidays, {}".format(name))
else:
    print("Sorry you are not in our age limit to enjoy the holiday")
