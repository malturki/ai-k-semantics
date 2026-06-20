x = 7
odds = {n * n for n in range(6) if n % 2}
result = odds == {1, 9, 25} and x == 7

letters = {c + "!" for c in "abcd" if c in "bd"}
result = result and letters == {"b!", "d!"}

parity = {n % 2 for n in [0, 1, 2, 3, 4] if n > 1}
result = result and parity == {0, 1}

empty = {n for n in range(3) if False}
result = result and empty == set()

truthy = {n for n in [0, 1, 2] if n}
result = result and truthy == {1, 2}

assert result
result
