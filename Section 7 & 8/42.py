# ipAdress = input("Please enter an IP Address")
# print(ipAdress.count("."))

parrot_list = ["no pinin", "no more", "what the f", "happy parrot"]
parrot_list.append("WOA")
for state in parrot_list:
    print("This parrot is " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
# numbers.sort()
print(numbers)
# print(numbers.sort())     This wouldn't work, works on object but does not create a new object
# objected has been updated but new one not created

print(sorted(numbers))   # works :)

numbers_in_order = sorted(numbers)

if numbers == numbers_in_order:     # Lists must be in same order to be equal
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbers_in_order == sorted(numbers):
    print("The lists are equal")
else:
    print("Not equal man")