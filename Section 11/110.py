# Scope and Recursion

# A recursive function is a function that calls itself


def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fib(n):
    """ F(n) = F(n-1) + F(n-2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibo(n):
    """ F(n) = F(n-1) + F(n-2) no recursion"""
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(30):
    # print(i, fact(i))
    # print(i, factorial(i))
    print(i, fib(i))
    print(i, fibo(i))

# recursive function was significantly slower for fibonacci sequence
