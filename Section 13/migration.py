from Section_12 import polymorphism

flock = polymorphism.Flock()
donald = polymorphism.Duck()
daisy = polymorphism.Duck()
duck3 = polymorphism.Duck()
duck4 = polymorphism.Duck()
duck5 = polymorphism.Duck()
duck6 = polymorphism.Duck()
duck7 = polymorphism.Duck()
percy = polymorphism.Penguin()
# mally = polymorphism.Mallard()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
# flock.add_duck(mally)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()

# stack trace comes after other functions even if it prints first. For example 4 ducks fly before the error
# even if the stack trace prints first!
