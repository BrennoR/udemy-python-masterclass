fruit = {"orange": "a sweet, orange, citrus, fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "citrus fruit"}

print(fruit)

veggies = {"cabbage": "everyones favorite",
           "sprouts": "really lovely",
           "spinach": "can I have some more fruit please"}

print(veggies)

# print(fruit.update(veggies))      returns none
# print(fruit)                      returns both combined

veggies.update(fruit)       # combines two dictionaries
# A new dictionary is not returned with update(), similar to sort
print(veggies)

nice_and_nasty = fruit.copy()       # originals are preserved
nice_and_nasty.update(veggies)
print(nice_and_nasty)


## DICTIONARY CHALLENGE ##

locations = {0: "You are sitting in front of a computer learning python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}

vocabulary = {"WEST": "W",
         "EAST": "E",
         "SOUTH": "S",
         "NORTH": "N",
         "QUIT": "Q",
         "ROAD": "1",
         "HILL": "2",
         "BUILDING": "3",
         "VALLEY": "4",
         "FOREST": "5"}

# print(locations[0].split())                 # AWESOME
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    # Pass the user input, using our words dictionary if necessary

    if len(direction) > 1:
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("We cannot go in that direction")