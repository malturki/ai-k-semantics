x = 7
squares = {n * n for n in range(5)}
result = squares == {0, 1, 4, 9, 16} and x == 7

letters = {c + "!" for c in "aba"}
result = result and letters == {"a!", "b!"}

parity = {n % 2 for n in [0, 1, 2, 3]}
result = result and parity == {0, 1}

empty = {n for n in range(0)}
result = result and empty == set()

assert result
result
