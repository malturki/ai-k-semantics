items = (1, 2)

items * 3 == (1, 2, 1, 2, 1, 2) and 3 * items == (1, 2, 1, 2, 1, 2) and items * 1 == items and items * 0 == () and items * -2 == () and items * True == items and False * items == () and len(items * 3) == 6
