low = 1
high = 1000

print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")

guesses_count = 1
while True:
    print("\tGuessing in the range of {} and {}".format(low,high))
    computer_guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess is correct "
                     .format(computer_guess).casefold())

    if high_low == "h":
        # Guess higher. The lower end of the range becomes one greater than the guess.
        low = computer_guess + 1
    elif high_low == "l":
        # Guess higher. The higher end of the range becomes one less than the guess.
        high = computer_guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses_count))
        break
    else:
        print("Please enter h, l, or c")
    guesses_count += 1
