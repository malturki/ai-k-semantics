x = 7
odds = {n: n * n for n in range(6) if n % 2}
result = odds == {1: 1, 3: 9, 5: 25} and x == 7

letters = {c: c + "!" for c in "abcd" if c in "bd"}
result = result and letters == {"b": "b!", "d": "d!"}

duplicate = {n % 2: n for n in [0, 1, 2, 3, 4] if n > 1}
result = result and duplicate == {0: 4, 1: 3}

empty = {n: n for n in range(3) if False}
result = result and empty == {}

truthy = {n: n for n in [0, 1, 2] if n}
result = result and truthy == {1: 1, 2: 2}

assert result
result
