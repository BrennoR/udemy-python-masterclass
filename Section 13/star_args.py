# from __future__ import print_function     IF python 2
# from __future__ import division

# print("Hello", "planet", "Earth")

# *args lets a function or method take a variable number of arguments


def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


print(average(1, 2, 3, 4))

# Challenge


def build_tuple(*args):
    return args


print(build_tuple(1, 2, 3, 4))
print(build_tuple('hey', 'wow', 'bam'))
print(type(build_tuple(45, 2)))


def average_word_length(*args):
    sum = 0
    for arg in args:
        sum += len(arg)

    return sum / len(args)


print(average_word_length('hello', 'hi', 'woa'))


def smallest_number(*args):
    return min(args)


print(smallest_number(2, 3, 7, 10))


def largest_number(*args):
    return max(args)


print(largest_number(9, 10, 80, 7))


def reverse_words(*args):
    for arg in args:
        print(arg[::-1], end=' ')


print(reverse_words('jello', 'hundred', 'pyrenee'))


words = ['hi', 'ohio', 'jelly', 'no']
print(words)
print(*words)   # unpacks list!
