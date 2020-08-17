for i in range(1, 13):
    print("No. {} squared is {} and cuded is {}".format(i, i ** 2, i ** 3))
print("*" * 80)

name = input("Enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print('You are eligible to vote {0}'.format(name))
#     print('Please put an X in the box')
# else:
#     print('Please comeback in {0} years'.format(18-age))

if age < 18:
    print('Please comeback in {0} years'.format(18-age))
elif age == 900:
    print('Sorry, Yoda, you die in Return of Jedi')
else:
    print('You are eligible to vote {0}'.format(name))
    print('Please put an X in the box')
