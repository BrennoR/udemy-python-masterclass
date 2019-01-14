for num in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(num)

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:   # unpack the tuple
    print(x, y)

times = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(times)

for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):   # Generator Expression, no need to create list!
    print(x, y)

# Use generator expression rather than a list comprehension if you are not going to be using the list more than once
