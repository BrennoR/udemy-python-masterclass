## Shelve Module ##

import shelve

with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "sour, yellow, citrus fruit"
    fruit['grape'] = "small sweet fruit growing in bunches"
    fruit['lime'] = "a sour green citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])

# print(fruit["grape"])           # outside with... throws error
print(fruit)

# Can't initialize a shelve using a literal, ex -> fruit = { "orange": "Citrus jawn", "Apple": "the other one"}

# fruit = shelve.open('ShelfTest')          Alternate
# fruit['orange'] = 'a citrus jawn'
# fruit.close()


with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    print(bike["colour"])
    print(bike["engine_size"])

with shelve.open("bike2") as bike2:              # throws error due to engine_size
    # bike2["make"] = "Honda"
    # bike2["model"] = "250 Dream"
    # bike2["colour"] = "red"
    # bike2["engin_size"] = 250
    # bike2["engine_size"] = 250                # after creating again, engin_size still there

    # del bike2["engin_size"]

    for key in bike2:                           # prints the keys in bike2
        print(key)

    print("=" * 40)

    print(bike2["colour"])
    # print(bike2["engin_size"])
    print(bike2["engine_size"])

fruit2 = shelve.open("fruit2")
fruit2["apple"] = "this is an apple"
fruit2["spam"] = "spam is a jawn"
fruit2["apple"] = "second apple as test"        # overwrites first apple

for snack in fruit2:
    print(snack + ": " + fruit2[snack])

print("=" * 50)

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit2:
#         description = fruit2[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

ordered_keys = list(fruit2.keys())
ordered_keys.sort()

for f in ordered_keys:                      # sorted method
    print(f + " - " + fruit2[f])

for v in fruit2.values():
    print(v)

print(fruit2.values())
#
for f in fruit2.items():
    print(f)

print(fruit2.items())

fruit2.close()

## A shelve key must be a string!!!!