text = ""
for a, b in ["ab", "cd"]:
    text += a + b

result = text == "abcd"

for a, *rest in ["xyz"]:
    result = result and a == "x" and rest == ["y", "z"]

for *letters, in ["q"]:
    result = result and letters == ["q"]

for *letters, in [""]:
    result = result and letters == []

for (c, d), in [("ef",)]:
    result = result and c == "e" and d == "f"

total = 0
for a, b in [range(2), range(2, 4)]:
    total += a * 10 + b

result = result and total == 24

for first, *rest in [range(3, 0, -1)]:
    result = result and first == 3 and rest == [2, 1]

for (m, n), in [(range(5, 7),)]:
    result = result and m == 5 and n == 6

empty_string_else = False
for a, in "":
    empty_string_else = False
else:
    empty_string_else = True

empty_range_else = False
for a, in range(0):
    empty_range_else = False
else:
    empty_range_else = True

result = result and empty_string_else and empty_range_else
assert result
result
