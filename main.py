import itertools


def is_collinear(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])


def slope(x1, y1, x2, y2):
    try:
        m = (y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        m = 0

    return m


SAMPLES = {
    "1": [(-1, -1), (1, 1), (2, 2), (3, 3), (3, 5)],
    "2": [(-1, 4), (1, 5), (2, 6), (11, 3), (11, 5), (3, 0), (1, 2), (4, -1)],
    "3": [
        (3, 1),
        (5, 2),
        (7, 3),
        (3, 5),
        (8, 10),
        (-1, -1),
        (1, 1),
        (2, 2),
        (3, 3),
        (3, 5),
    ],
}

if __name__ == "__main__":

    print("Enter 1 for sample: (-1,-1), (1,1), (2,2), (3,3), (3,5)")
    print(
        "Enter 2 for sample: (-1,4), (1,5), (2,6), (11,3), (11,5), (3,0), (1,2), (4, -1)"
    )
    print(
        "Enter 3 for sample: (3,1), (5,2), (7,3), (3,5), (8, 10), (-1,-1), (1,1), (2,2), (3,3), (3,5)"
    )
    print("Your choice:")

    while True:
        choice = input()

        try:
            points = SAMPLES[choice]
        except KeyError:
            print("Wrong choice!")
            break

        results = []

        for item in itertools.combinations(points, 3):
            a, b, c = item
            if is_collinear(a, b, c):
                _m = slope(a[0], a[1], b[0], b[1])
                _b = a[1] - _m * a[0]
                results.append((_m, _b))

        print("Solutions:")
        for s in set(results):
            print(f"m={s[0]}, b={s[1]}")

        print("Try again, enter your choice:")
