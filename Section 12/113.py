a = 12
b = 4
print(a + b)
print(a.__add__(b))

# EVERYTHING IN PYTHON IS AN OBJECT


class Kettle(object):

    power_source = 'electricity'

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False             # In class, use only one line between methods

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable bound to an instance of a class.
"""

# In python a class is also the same thing as a type, every type is a class

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

# The term constructor, refers to a special method that is executed when the instance of a class is created (__init__)

Kettle.switch_on(kenwood)       # This time a parameter for the object IS needed
print(kenwood.on)

print("+" * 80)

kenwood.power = 1.5     # This works!
print(kenwood.power)
# print(hamilton.power)   # This throws an error

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# namespaces
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switch to atomic power")
Kettle.power_source = "atomic"

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# namespaces
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switch Kenwood to gas")
kenwood.power_source = 'gas'
print(kenwood.__dict__)
print(Kettle.__dict__)
print(kenwood.power_source)

# Encapsulation - Objects contain the data and the methods that run on that data, and don't expose the actual
# implementation to the outside world.
