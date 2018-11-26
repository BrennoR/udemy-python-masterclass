## Sets ##

farmAnimals = {"sheep", "cow", "hen"}
print(farmAnimals)

for animal in farmAnimals:
    print(animal)

print("=" * 40)

wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wildAnimals)

for animal in wildAnimals:
    print(animal)

farmAnimals.add("horse")
wildAnimals.add("horse")
print(farmAnimals)
print(wildAnimals)

# No inherent ordering with sets

# Empty set must be made with set function, empty {} creates an empty dictionary

emptySet = set()
emptySet2 = {}      # creates empty dictionary
emptySet.add("hi")
# emptySet2.add("HI")   # doesn't work

# even = set(range(0, 40, 2))         # can create sets from ranges and tuples
# print(even)                         # also unordered
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)

even = set(range(0, 40, 2))
print(even)
print(len(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(squares)
print(len(squares))

print(even.union(squares))          # joins the two sets
print(len(even.union(squares)))     # adds the two sets but duplicates stay single

print("=" * 40)

print(even.intersection(squares))       # numbers present in both sets
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("=" * 40)

even = set(range(0, 40, 2))
print(sorted(even))

squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(sorted(squares.difference(even)))
print(squares - even)


## Sets 2 ##

print("=" * 80)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)     # actually changes the even set, removes from the even set
# print(sorted(even))

even = set(range(0, 40, 2))
print(sorted(even))
squaresTuple = (4, 6, 9, 16, 25)
squares = set(squaresTuple)
print(sorted(squares))

# print("symmetric even minus squares")                   # removes items belonging to both sets
# print(sorted(even.symmetric_difference(squares)))       # everything but the intersection numbers
#
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))       # can also use carrots to perform this function

# always sort if needed to sort, sometimes bugs sort automatically??

squares.discard(4)
squares.remove(16)
squares.discard(8)          # no error, does nothing, 8 not in set
print(squares)
# squares.remove(8)           # throws error, 8 not in set

# if 8 in squares:            # fix for remove
#     squares.remove(8)

# sometimes you may want an error when removing, remove can be useful there, python provides ways to raise an exception

try:                        # method to trap the error
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of squares set")


## supersets and subsets

print("=" * 80)

even = set(range(0, 40, 2))
print(sorted(even))
squaresTuple = (4, 6, 16)
squares = set(squaresTuple)
print(sorted(squares))

if squares.issubset(even):                  # subset = all its members contained in another set
    print("squares is a subset of even")

if even.issuperset(squares):                # superset - all the members of another set contained in itself
    print("even is a superset of squares")

# frozen set - immutable set
# no add, remove, discard with frozen set

even2 = frozenset(range(0, 100, 2))
print(even2)

# even2.add(3)          throws error, frozenset

# can call difference, intersection, symmetric but not the update variations



## Challenge ##

# vowels = {"a", "e", "i", "o", "u"}        my solution
vowels = frozenset("aeiou")
print(vowels)

text = set(input("Enter some text").lower())

finalSet = text.difference(vowels)

finalSet.discard(' ')

finalList = sorted(finalSet)
print(finalList)
