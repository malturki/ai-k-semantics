empty = set()
nonempty = {1, 2, 1}

result = len(empty) == 0 and not empty and 1 not in empty and empty == set() and empty != nonempty and empty < nonempty and empty <= nonempty and empty <= set() and nonempty > empty and nonempty >= empty
assert result
result
