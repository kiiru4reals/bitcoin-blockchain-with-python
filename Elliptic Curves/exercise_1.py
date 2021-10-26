from cprint import cprint

def test(x, y):
    return pow(y, 2) == pow(x, 3) + 5 * x + 7

points = [(2, 1), (-1, -1), (18, 77), (5, 7)]


if __name__ == '__main__':
    for count, a in enumerate(points, start=1):
        if test(a[0], a[1]):
            cprint(f'{count}. {a}\t\t: True', c='Ig')
        else:
            cprint(f'{count}. {a}\t\t: False', c='rI')