import collect_your_thoughts as cyt

print(
'''Welcome to Getting things Done Projec
1. Enter your thoughts
''')
inPile = []
while True:
    print('''Please choose from the options below
    * Press 1 to enter your thoughts/todo's/events/ideas/projects etc
    * Press 2 to Exit application''')

    selection = input("-->  ")

    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 and 2")
        continue
    if entry == 1:
        print("Do you want to enter Multiple Thoughts?")
        selection = input("'Y' or 'N'--> ").capitalize()
        if selection == 'Y':
            #more_choices = False
            while True:
                thought = input("--> ")
                #print(thought)
                inPile.append(thought)
                more = input("More inputs press 'Y' To stop press 'N' --> ").capitalize()
                if more == 'N':
                    break
                elif more == 'Y':
                    continue
                else:
                    print("Invalid Choice...")
                    break
        else:
            thought = input("--> ")
            inPile.append(thought)
        print("Thanks for capturing your ideas,thoughts,todo's etc...")
        print(f"Below is your list we will be working on: ")
        i = 1
        for entry in inPile:
            print(f'{i}. {entry}')
            i += 1
        print('*'*50)
    elif entry == 2:
        print("Exiting program...")
        break
    else:
        print("Only 1 and 2 are valid choices")
