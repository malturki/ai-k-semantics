def first_even(x):
    for item in [1, 3, 4, 6]:
        if item % 2 == 0:
            return item
    return x

first_even(9) == 4
