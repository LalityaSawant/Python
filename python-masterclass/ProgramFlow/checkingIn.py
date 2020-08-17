parrot = "Norwegian Blue"

letter = input("Enter s character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

print()

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to cinema")
