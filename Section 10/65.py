## Writing ##

# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt",'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)         # = here is not assignment operation but a named argument (city_file)

# write puts programs in a buffer so the python code here will finish but if the content is large, it will keep writing
# to file until it is done... Data is written to buffer and then the contents of the buffer is transferred to the
# external device in the background

# look into flush= command

# cities = []
#
# with open("cities.txt",'r') as city_file:
#     for city in city_file:
#         cities.append(city.strip('\n'))     # removes \n, python automatically handles different conventions for line
#                                             # breaks found in other operating systems
# print(cities)
# for city in cities:
#     print(city)


# print('Adelaide'.strip('A'))        # removes characters from the beginning or end of a string but only from the
#                                     # beginning or end
# print('Adelaide'.strip('del'))

# imelda = "More Mayhem", "Imelda May", "2011", ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)               # eval is not a good idea for this...

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
