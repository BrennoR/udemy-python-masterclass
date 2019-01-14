import timeit

text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words

# use map


def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w


# for x in map(str.upper, text.split(' ')):
#     print(x)


if __name__ == "__main__":
    result_1 = timeit.timeit(comp_caps, number=100000)
    result_2 = timeit.timeit(comp_words, number=100000)
    result_3 = timeit.timeit(map_caps, number=100000)
    result_4 = timeit.timeit(map_words, number=100000)
    print("Capitals: {}".format(result_1))
    print("Words: {}".format(result_2))
    print("Map Capitals: {}".format(result_3))
    print("Map Words: {}".format(result_4))
