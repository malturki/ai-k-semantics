items = (0, 1, 2, 3, 4)

items[1:4] == (1, 2, 3) and items[:2] == (0, 1) and items[3:] == (3, 4) and items[:] == items and items[-4:-1] == (1, 2, 3) and items[-99:99] == items and items[4:2] == () and len(items[1:4]) == 3
