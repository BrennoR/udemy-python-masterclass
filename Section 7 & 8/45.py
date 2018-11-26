# Iterators

string = "1234567890"
#
# for char in string:
#     print(char)
#
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# print(next(my_iterator))  Provides error because no more errors

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)



# Challenge

my_list = ["ducks", "penguins", "bears", "pandas", "hummingbirds", "jaguars", "whales"]
my_iterator = iter(my_list)

for n in range(len(my_list)):
    print(next(my_iterator))

for animal in my_list:      # Normal way
    print(animal)