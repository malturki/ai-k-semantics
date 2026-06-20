x = 99
values = {n % 2: n for n in range(6) if n if n < 5}
result = values == {1: 3, 0: 4} and x == 99

letters = {c: c + "!" for c in "abcd" if c in "bcd" if c != "c"}
result = result and letters == {"b": "b!", "d": "d!"}

empty = {n: n for n in range(5) if n if n < 0}
result = result and empty == {}

assert result
result
