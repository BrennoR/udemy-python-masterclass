a = 2
b = 3
print("a is {}, b is {}".format(a, b))

a, b = b, a     # In python the right hand side is evaluated first (ex. a, b = 3, 2 is equivalent)
# temp = a      code needed to do same thing in some other languages
# a = b
# b = temp
print("a is {}, b is {}".format(a, b))
