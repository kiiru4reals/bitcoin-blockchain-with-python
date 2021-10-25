test = [7, 11, 17, 31]

for x in test:
    print([pow(y, x - 1, x) for y in range(1, x)])