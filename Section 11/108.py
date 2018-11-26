# Importing Techniques

import blackjack
# from blackjack import *        # everything from blackjack module namespace now appears here
                                 # but does not import methods that start with an underscore

# g = sorted(globals())
# for x in g:
#     print(x)

# print(__name__)
#
blackjack._deal_card(blackjack.dealer_card_frame)
blackjack.play()

# convention is to use an underscore after a name if it would otherwise conflict with a function that is
# built into python

# Python has no concept of private or protected variables - deal_card method

# starting a name with an underscore means that it was intended to be protected, not used outside of the module
# that it was created in

# starting a name with two underscores invokes python's name mangling rules

# names that start and end with two underscores are basically things that should never be changed

personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details     # underscore here means code is not interested in age (24)
print(name, country)

# the point here is the underscore is a way to name something as a throw away value that you know you will not be using
# two underscores alone also used for this purpose ^

# double underscore can also be called 'dunder'

# example for name mangling with two underscores:
# class: Test
# variable: __baz
# Test.__baz returns error because name was mangled to _Test__baz
# Test._Test__baz returns correct variable
