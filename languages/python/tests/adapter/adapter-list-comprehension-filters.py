x = 7
values = [n for n in range(8) if n % 2 if n > 3]
result = values == [5, 7] and x == 7

letters = [c + "!" for c in "abcd" if c in "bcd" if c != "c"]
result = result and letters == ["b!", "d!"]

empty = [n for n in range(5) if n if n < 0]
result = result and empty == []

assert result
result
