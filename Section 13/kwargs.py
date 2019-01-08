def print_backwards(*args, file=None):
    for word in args[::-1]:
        print(word[::-1], end=' ', file=file)


print_backwards("Hello", "planet", "Earth", "take", "me", "to", "your", "leader")

with open("backwards.txt", 'w') as backwards:
    print_backwards("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", file=backwards)

# ** unpacks a dictionary


def print_backwards_2(*args, end=' ', **kwargs):
    print(kwargs)
    # kwargs.pop('end', None)     # Works as well
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)


with open("backwards_2.txt", 'w') as backwards:
    print_backwards_2("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", file=backwards, end='\n')

print()
print("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", end='\n', sep='|')
print_backwards_2("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", end='\n', sep='|')


def print_backwards_3(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:    # Change the range
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)   # And print the first word separately


print('\n')
print("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards_3("Hello", "planet", "Earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)


# Good way to do it!
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)
