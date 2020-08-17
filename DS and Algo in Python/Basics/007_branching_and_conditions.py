print("welcome to calc program")
print('-'*30)
choice = int(input("Choose 1 to multiply, 2 to divide-> "))
if choice == 1 or choice == 2:
    num_1 = int(input('Enter first num-> '))
    num_2 = int(input('Enter second num-> '))
    if choice == 1:
        print(f'{num_1} multipled by {num_2} is {num_1*num_2}')
    else:
        print(f'{num_1} divided by {num_2} is {num_1/num_2}')
else:
    print('Invalid choice')
