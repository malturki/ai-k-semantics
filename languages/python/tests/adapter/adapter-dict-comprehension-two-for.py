x = 77
values = {i * 10 + j: i + j for i in range(4) for j in range(i)}
result = values == {10: 1, 20: 2, 21: 3, 30: 3, 31: 4, 32: 5} and x == 77

dupes = {j: i for i in range(3) for j in range(2)}
result = result and dupes == {0: 2, 1: 2}

letters = {a + b: b + a for a in "ab" for b in "xy"}
result = result and letters == {"ax": "xa", "ay": "ya", "bx": "xb", "by": "yb"}

empty = {i: j for i in range(3) for j in range(0)}
result = result and empty == {}

assert result
result
