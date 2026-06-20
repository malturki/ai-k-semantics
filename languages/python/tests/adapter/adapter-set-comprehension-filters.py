x = 42
values = {n % 3 for n in range(8) if n if n > 3}
result = values == {0, 1, 2} and x == 42

letters = {c + "!" for c in "abcd" if c in "bcd" if c != "c"}
result = result and letters == {"b!", "d!"}

empty = {n for n in range(5) if n if n < 0}
result = result and empty == set()

assert result
result
