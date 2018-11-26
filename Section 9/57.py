# myList = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
#
# newString = ''
# # for c in myList:            # BAD BAD BAD!!!! inefficient
# #     newString += c + ", "
#
# newString = ", ".join(myList)
# print(newString)
#
# newerString = ", ".join(letters)
# print(newerString)
#
# numbahString = " mississippi ".join(numbers)
# print(numbahString)

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    # availableExits = ""                           BAD BAD
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())       # GOOD

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("We cannot go in that direction")


# EXIT IS A KEY WORD IN PYTHON THAT WILL CAUSE THE PROGRAM TO END IMMEDIATELY