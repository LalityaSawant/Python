import myList as ml

def capture_ideas():

    inPile = ml.MyList()
    #print(f'type(inPile): {type(inPile)}')

    print("Do you want to enter Multiple Thoughts?")
    selection = input("'Y' or 'N'--> ").capitalize()
    if selection == 'Y':
        #more_choices = False
        while True:
            thought = input("--> ")
            #print(thought)

            inPile.setMyList(thought)   # inPile.append(thought)
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
        inPile.setMyList(thought)  #inPile.append(thought)
    print("Thanks for capturing your ideas,thoughts,todo's etc...")

    return inPile.getMyList()
