# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
# another_even = even
#
# another_even = list(even)   # New list
# another_even2 = sorted(even, reverse=True)   # Also new list
#
# print(another_even is even)     # Same variable/thing
# print(another_even == even)     # Same content
#
# print("another_even 2")
# print(another_even2 is even)     # Same variable/thing
# print(another_even2 == even)     # Same content
#
# another_even.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]   # A list containing two lists
print(numbers)

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)