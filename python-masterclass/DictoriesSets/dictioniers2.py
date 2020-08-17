locations = {
    0: "In front of computer",
    1: "Road",
    2: "Hill",
    3: "Home",
    4: "Valley",
    5: "Forest"
}


exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}
         }

numExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
            2: {"5": 5},
            3: {"1": 1},
            4: {"1": 1, "2": 2},
            5: {"2": 2, "1": 1}
            }

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",
              "HILL": "2",
              "HOME": "3",
              "VALLEY": "4",
              "FOREST": "5"
              }

loc = 1
while True:
    availableExits = " , ".join(exits[loc].keys())

    # for direction in exits[loc]:
    #     availableExits += direction + ','

    print("You location is : {}".format(locations[loc]))

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(numExits[loc])

    playerDirection = input("Your available directions are {}, please select one : ".format(availableExits)).upper()

    if len(playerDirection) > 1:
        words = playerDirection.split()
        for word in words:
            if word in vocabulary:
                playerDirection = vocabulary[word]

    print(loc)
    if playerDirection in allExits:
        loc = allExits[playerDirection]
    else:
        print("You  cannot go in that direction")
