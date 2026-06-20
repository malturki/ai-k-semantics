x = 7
squares = {n: n * n for n in range(4)}
result = squares == {0: 0, 1: 1, 2: 4, 3: 9} and x == 7

letters = {c: c + "!" for c in "ab"}
result = result and letters == {"a": "a!", "b": "b!"}

duplicate = {n % 2: n for n in [0, 1, 2, 3]}
result = result and duplicate == {0: 2, 1: 3}

assert result
result
