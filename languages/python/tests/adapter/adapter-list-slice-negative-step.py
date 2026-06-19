items = [0, 1, 2, 3, 4, 5]

items[::-1] == [5, 4, 3, 2, 1, 0] and items[5:1:-2] == [5, 3] and items[:1:-2] == [5, 3] and items[4::-2] == [4, 2, 0] and items[-1:-5:-1] == [5, 4, 3, 2] and items[99:-99:-3] == [5, 2] and len(items[::-1]) == 6
