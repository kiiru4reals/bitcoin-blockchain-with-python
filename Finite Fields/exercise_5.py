test = [1, 3, 7, 13, 18]
prime = 19

for x in test:
    print(sorted([x * y % prime for y in range(1, 20)]))
