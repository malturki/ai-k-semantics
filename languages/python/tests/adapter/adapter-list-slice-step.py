items = [0, 1, 2, 3, 4, 5]

items[::2] == [0, 2, 4] and items[1:6:2] == [1, 3, 5] and items[:5:2] == [0, 2, 4] and items[2::3] == [2, 5] and items[99:100:2] == [] and len(items[::2]) == 3
