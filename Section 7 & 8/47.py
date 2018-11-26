# decimals = range(0, 100)
# my_range = decimals[3:40:3]
# print(my_range == range(3, 40, 3))
#
# print(range(0, 5, 2) == range(0, 6, 2))  # Numbers are different but sequence of values is the same... aka: end result
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:   # starts from last number
#     print(i)
#
# print('=' * 50)
#
# for i in range(99, 0, -2):
#     print(i)
#
# print('=' * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))
#
# for i in range(0, 100, -2):     # start and end steps must correspond, aka 100 -> 0
#     print(i)
#
# for i in range(100, 0, -2):
#     print(i)

# back_string = "egaugnal lufrewop yrev a si nohtyP"
# print(back_string[::-1])
#
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

o = range(0, 100, 4)
print(o)                # range(0, 100, 4)
p = o[::5]
print(p)                # range(0, 100, 20)
for i in p:
    print(i)            # 0 20 40 60 80

my_range = range(0, 100, 7)
print(my_range)
second_range = my_range[::8]
print(second_range)             # range(0, 105, 56).... weird
for i in second_range:
    print(i)