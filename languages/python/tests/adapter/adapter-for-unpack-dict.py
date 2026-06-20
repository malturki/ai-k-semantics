total = 0
for a, b in {(1, 2): "x", (3, 4): "y"}:
    total += a * 10 + b

result = total == 46

for a, *rest in {(5, 6, 7): "z"}:
    result = result and a == 5 and rest == [6, 7]

for (ka, kb), in {((8, 9),): "w"}:
    result = result and ka == 8 and kb == 9

empty_else = False
for a, b in {}:
    empty_else = False
else:
    empty_else = True

result = result and empty_else
assert result
result
