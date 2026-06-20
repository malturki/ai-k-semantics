x = 64
values = {i * 10 + j for i in range(4) for j in range(i)}
result = values == {10, 20, 21, 30, 31, 32} and x == 64

dupes = {j for i in range(3) for j in range(2)}
result = result and dupes == {0, 1}

letters = {a + b for a in "ab" for b in "xy"}
result = result and letters == {"ax", "ay", "bx", "by"}

empty = {i for i in range(3) for j in range(0)}
result = result and empty == set()

assert result
result
