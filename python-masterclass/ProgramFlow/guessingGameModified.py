import random
min_num = 1
max_num = 10
answer = random.randint(min_num,max_num)
# print('Hint: {}'.format(answer))  # TODO: Remove after testing
guess = 0  # initialize to any number != answer
i = 0

print("Please guess number between {0} and {1}: ".format(min_num,max_num))

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    i += 1
    if guess == answer:
        print("Well done, you guessed it {0} time".format(i))
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be > answer
            print("Please guess lower")
    #     guess = int(input())
    #     i += 1
    #     if guess == answer:
    #         print("Well done, you guessed it {0} time".format(i))
    #         break
    #     else:
    #         print("Sorry, you have not guessed correctly")
    # continue
