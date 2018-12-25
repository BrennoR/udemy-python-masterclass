# x = 8 = 5 # Syntax Error
x = 8
# y = x / 0   # Exception: division by zero


def factorial(n):
    # n! can also be defined as n * (n - 1)!
    """ Calculates n recursively """
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n - 1)


try:
    print(factorial(900))  # Recursion Error if no try block
except (RecursionError, ZeroDivisionError):     # Use separate except clauses if responses should be unique
    print("This program cannot calculate factorials that large")
# except ZeroDivisionError:
#     print("Can't divide by zero!")

print("Program terminating")

# Overflow will probably not happen using Python, Python can calculate gigantic numbers, 900! for example which is
# leaps and bounds larger than the estimated number of atoms in the universe
