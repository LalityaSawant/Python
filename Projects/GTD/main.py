import collect_your_thoughts as cyt
import myList as mcl

print('''
Welcome to Getting things Done Project
1. Enter your thoughts
2. Review your thoughts
''')

inPileList = mcl.MyCompleteList()
while True:
    # inPileList = mcl.MyCompleteList()
    print('''Please choose from the options below
    * Press 1 to enter your thoughts/todo's/events/ideas/projects etc
    * Press 2 to start reviewing your items
    * Press 9 to Exit application''')

    selection = input("-->  ")

    try:
        entry = int(selection)
    except ValueError:
        print("Please enter a number between 1 and 2")
        continue
    if entry == 1:
        inPileList.setMyCompleteList(cyt.capture_ideas())
        print(f"Below is your list we will be working on: ")
        i = 1
        for entry in inPileList.getMyCompleteList():
            print(f'{i}. {entry}')
            i += 1
        print('*' * 50)
    elif entry == 2:
        print("We will be reviewing your items for prioritisation !!")
    elif entry == 9:
        print("Exiting program...")
        break
    else:
        print("Only 1/2 and 9 are valid choices")
