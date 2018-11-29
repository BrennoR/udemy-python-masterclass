# Polymorphism - The ability of objects to have different forms
# ex: int is a number that can be used to perform arithmetic but it is also something that can be printed

# a = 3           # int
# b = "tim"       # str
# c = 1, 2, 3     # tuple
#
# print(a)
# print(b)
# print(c)

# Overloading Methods - You create different versions of the method that take different parameters,
# and the compiler decides which one to use based on the number and type of the parameters passed to it.

# ^^^ Not possible in Python and not necessary either!

# The str function can cope with anything that is passed to it because whatever it is, it is guaranteed
# to have a str method. This is because everything in Python is an object and inherits from Object!


# Duck Test #

class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weeeee this is fun!")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying.")
        else:
            print("I think I'll just walk")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)          # When a class contains another object like this, it is called Composition!

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's lovely")

    def quack(self):
        print("Quack quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a larf? I'm a penguin!")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    # test_duck(donald)

    donald.fly()
    #
    # percy = Penguin()
    # test_duck(percy)

# Python is a dynamically typed language which is sometimes referred to as a duck type
# Here, as far as python is concerned... percy is a duck!

# is-a relationship = Inheritance
# has-a relationship = Composition

