fruit = {"orange": "a sweet, orange, citrus, fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "citrus fruit"}

print(fruit)
print(fruit["orange"])

bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

# Dictionary keys must be immutable!

fruit["pear"] = "an odd shaped apple"   # Method to add values to dictionary
print(fruit)

# Keys in dictionaries are unique, if you sign a value to an existing key it will replace the value
fruit["pear"] = "this is replaced"
print(fruit)

# fruit = {"orange": "a sweet, orange, citrus, fruit",
#          "apple": "good for making cider",
#          "lemon": "a sour, yellow citrus fruit",
#          "grape": "a small, sweet fruit growing in bunches",
#          "lime": "citrus fruit",
#          "apple": "round and crunchy"}        apple will take the last entry!

# Remove items

del fruit["lemon"]
print(fruit)

# del fruit         deletes the variable/dictionary completely
# print(fruit)

# fruit.clear()     removes all entries in the dictionary but keeps the variable
# print(fruit["tomato"])      # returns an error, tomato doesn't exist in dictionary

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     # fruit.has_key(dict_key)       Python 2, deprecated
#     print(description)
#     # if dict_key in fruit:         ^ Python 3 method
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#     #     print("we don't have a " + dict_key)

# for snack in fruit:
#     print(fruit[snack])

# no guarantee items in dictionary keep order, hesh functions, used in cryptography

# for i in range(10):             # the slots are arbitrarily created when the dictionary is created, so these will be
#     for snack in fruit:         # the same, but when ran again, they will change
#         print(snack + " is " + fruit[snack])
#     print('=' * 40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()                 # same order every time
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):        for sorting
# for f in fruit:                       # where sorting is unnecessary
#     print(f + " - " + fruit[f])

# for val in fruit.values():
#     print(val)

# better to use keys when possible, this val way is not optimized and less efficient

# print("=" * 40)
# for key in fruit:       # Much more efficient
#     print(fruit[key])
#
# fruit_keys = fruit.keys()
# print(fruit_keys)       # we get a view object
#
# fruit["tomato"] = "Not nice with ice cream"
#
# print(fruit_keys)       # adding an item changes fruit_keys automatically

# print(fruit.keys())
# print(fruit.values())

print("-" * 40)
print(fruit)
print(fruit.items())        # can produce a tuple from it

f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

# can produce a dictionary from tuple as well

print(dict(f_tuple))