# Functions #


def python_food():
    width = 80
    text = "Spam and Eggs"
    left_margin = (width - len(text)) // 2      # // - Integer division
    print(" " * left_margin, text)


def center_text(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
# python_food()
# print(python_food())    # function is executed and what the function returns is also outputed

center_text("Spam and Eggs")
center_text("Spam, spam and jawn")
center_text("This is pretty cool I guess")
center_text(12)           # throws error
# center_text()             # missing argument, returns error

# parameter refers to text on line 11 for example and arguments are the actual values called when function is used
# for example "Spam and Eggs" on line 18
# They are usually used interchangebly in the real world

print("first", "three", 4, 15)


def center_text2(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


center_text2("New Test")
center_text2("first", "three", 4, 15)


# def center_text3(*args):              # doesn't create expected result
#     text = " ".join(str(args))
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)


# center_text3("second", "woa", 4, 3)

def center_text4(*args, sep=' ', end='\n', centered_file=None, flush_me=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=centered_file, flush=flush_me)


center_text4("first", "three", 4, 15, sep=':')

# two functions that take the exactly same parameters are said to have the same exact signature

with open("centered", mode='w') as center_file:
    center_text4("Ham and Jam", centered_file=center_file)
    center_text4("WOA and WOW", centered_file=center_file)
    center_text4("HE AND HA", centered_file=center_file)


def center_text5(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


print(center_text5("Ham and Jam"))
center_text5("WOA and WOW")
print(center_text5("HE AND HA"))
print(center_text5("first", "three", 4, 15, sep=':'))

print("=" + str(12 * 3))
print(sorted(["b", "c", "d", "a"]))

s1 = center_text5("walrus")
s2 = center_text5("potato")
s3 = center_text5("tomato")
s4 = center_text5("penguin")

print(s1)
print(s1, s2, s3, s4)

with open("menu", 'w') as menu:
    s1 = center_text5("walrus")
    print(s1, file=menu)
    s2 = center_text5("potato")
    print(s2, file=menu)
    s3 = center_text5("tomato")
    print(s3, file=menu)
    s4 = center_text5("penguin")
    print(s4, file=menu)
    print(center_text5("This is the one without the var"), file=menu)
