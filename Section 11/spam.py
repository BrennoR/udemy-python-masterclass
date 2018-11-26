
def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more " + x    # y must exist before spam3() is called
        y += spam3()        # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    # x = "spam" + spam2()        # breaks because spam2() tries to use the value of x when it is called, but x does not
    x = "spam"      # x must exist before spam2() is called
    x += spam2()    # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))   # yet have a value
    return x


print(spam1())

# wherever possible, try to write functions so that they only use local variables and parameters
# only access global and nonlocal variables when it is absolutely necessary
# no matter how trivial the change you make, test the program thoroughly to make sure nothing has been broken
# often simple changes will break code
# if you write unexpected code, make sure to write a comment so the next person who looks at the code understands it
# and doesn't mess it up

# at the module level, the local scope is the same as the global scope
print(locals())
print(globals())

# free variables are returned by locals() when it is called in function blocks, but not in class blocks

# order in which python searches for names: local -> enclosing (nonlocal or free) -> global -> built_ins (python stuff)
