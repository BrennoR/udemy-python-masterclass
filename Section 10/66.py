for i in range(2,13):
    for j in range(1,13):
        print("{:>2} times {:<2} is {:<3}".format(j,i,i*j))
    print('-' * 22)

with open('sample.txt', 'a') as sample_file:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0:<2} is {2:<3}".format(i, j, i * j), file=sample_file)
        print('-' * 22, file=sample_file)