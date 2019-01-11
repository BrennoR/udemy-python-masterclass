print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you it's square: "))

squares = [number ** 2 for number in numbers]   # list comprehension
# squares = {number ** 2 for number in numbers}   # set comprehension
# squares = [number ** 2 for number in range(1, 7)]

index_pos = numbers.index(number)
print(squares[index_pos])

# list comprehensions give automatic protection from side effects caused
# by bugs such as here where number is used twice
