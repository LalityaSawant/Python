truth_condition = True

if truth_condition:
    print("Truth")

choice = 2

if choice == 1:
    print("you have choosen option 1")
elif choice == 2:
    print("you have choosen option 2")
else:
    print('Invalid')

made_payment = True
a = 'Please pay monthly premium'
b = 'welcome to your homepage'

if not made_payment:
    print(a)
else:
    print(b)

i = 10
j = 10
k = 10

if i< j and i < k:
    print("i is less than j and k")
elif i ==j or i ==k:
    print("i is qual to either j or k")
elif i ==j and i ==k:
    print(" i is equal to j and k")
else:
    print("something else")

#ternary operator
print('-'*30)
print('Ternory opertor example')

course = 'java'
a = 'enrolled in python'
b = 'enrolled in some other course'

if course == 'python':
    print(a)
else:
    print(b)

#ternery operator
print(a) if course == 'python' else print(b)
