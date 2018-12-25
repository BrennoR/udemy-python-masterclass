import sys


def division():
    while True:
        try:
            a = int(input("Please enter a number: "))
            b = int(input("Please enter another number: "))
            print("{} divided by {} is {}".format(a, b, a / b))
            # break
        except ValueError:
            print("One number is invalid, please enter integers only")
        except ZeroDivisionError:
            print("Cannot divide by zero, please pick a second number higher or lower than zero")
            # sys.exit(1)
        except EOFError:
            sys.exit(0)
        else:   # MUST come after except and before finally. Will only execute if no break on try
            # only executes if the try block completed WITHOUT raising an exception
            print("Division performed successfully")
            return a / b
        finally:    # MUST come after all except clauses, is called regardless of try, except outcome
            print("The finally clause always executes")


division()

# command D (^D) signals to Python that there is no input left. Results in an EOF Error (End of File)

# can also just use except Exception: to catch everything. This is not recommended however, better to be specific.
# except: with no values catches everything!
