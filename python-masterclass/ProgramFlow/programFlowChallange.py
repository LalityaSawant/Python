# choice = -1
# while True:
#     if choice == 0:
#         print("Exiting the application...")
#         break
#     elif 1 <= choice <= 5:
#         print("You choose to {} ".format(choice))
#     else:
#         print("Please choose your option from the list below")
#         print("1.\tLearn Python")
#         print("2.\tLearn Java")
#         print("3.\tGo swimming")
#         print("4.\tHave dinner")
#         print("5.\tGo to bed")
#         print("0.\tExit")
#
#     choice = int(input())

# another and better way of writing above code
choice = -1
while choice != 0:
    if 1 <= choice <= 5:
        print("You choose to {} ".format(choice))
    else:
        print("Please choose your option from the list below")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to bed")
        print("0.\tExit")

    choice = int(input())
else:
    print("Exiting the application...")
