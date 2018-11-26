#### Tuples ####
# set of data that cannot be changed #

t = "a", "b", "c"       # Tuple
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))  # Tuple

# Recommended to use brackets/parentheses when creating a tuple ()  t = ("a", "b", "c")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets"  # Can't change items in Tuples -> Error

imelda = imelda[0], "Imelda May", imelda[2]
print(imelda)

# A type being immutable means you can't change the contents of an object once you created it
# but it doesn't mean that your variable can't be assigned a new object of that type

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

# expressions on the right-hand side of an assignment are always evaluated before the left-hand side

# Lists are intended to hold items of the same type while tuples are intended to hold heterogeneous items


a = b = c = d = 12
print(c)
a, b = 12, 13
print(a, b)
print(b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))

title, artist, year = imelda        # Unpacking the tuple [actual term]
print(title)
print(artist)
print(year)

metallica2.append("Rock")
# title, artist, year = metallica2    # Throws error, too many values to unpack

# imelda.append("Jazz")      Doesn't work

imelda2 = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),(2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")) # Parentheses very important here

imelda3 = "More Mayhem", "Imelda May", 2011, (1, "Pulling the Rug"),(2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")

print(imelda2)

# title, artist, year, tracks = imelda2
title, artist, year, track1, track2, track3, track4 = imelda3
print(title)
print(artist)
print(year)
print(track1)   # Tuple in its own right
print(track2)
print(track3)
print(track4)


# Challenge

title, artist, year, tracks = imelda2
print("{} by {}, {}".format(title,artist,year))
print("Tracks:")
for song in tracks:
    # print("\t", song)
    track, title = song
    print("\tTrack Number: {}, Title: {}".format(track, title))

# Tuples are immutable but a mutable object in a tuple such as a list, the mutable objects contents can be changed...