# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
from statistics import mean, stdev


setup = """\

"""

fact = """\
def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

x = fact(130)
"""

factorial = """\
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

y = factorial(130)
"""

result_1 = timeit.timeit(fact, number=10000)
result_2 = timeit.timeit(factorial, number=10000)
print("Iterative Approach: {}".format(result_1))
print("Recursive Approach: {}".format(result_2))


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
    print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))

    # importing from __main__ is equivalent to import from timeitchallenge, but if we import from __main__
    # then it works even if we rename the file

    print(timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=8))
    print(timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=8))

    list_1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=8)
    list_2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=8)
    print(sum(list_1))
    print(sum(list_2))

    print(mean(list_1), stdev(list_1))
    print(mean(list_2), stdev(list_2))
