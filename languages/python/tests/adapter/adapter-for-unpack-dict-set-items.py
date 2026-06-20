for a, b in [{"x": 1, "y": 2}]:
    result = a == "x" and b == "y"

for a, b in [{1, 2}]:
    result = result and {a, b} == {1, 2}

for first, *rest in [{"p": 1, "q": 2, "r": 3}]:
    result = result and first == "p" and rest == ["q", "r"]

for *keys, in [{}]:
    result = result and keys == []

for first, *rest in [{3, 4, 5}]:
    result = (
        result
        and len(rest) == 2
        and first in {3, 4, 5}
        and rest[0] in {3, 4, 5}
        and rest[1] in {3, 4, 5}
        and first not in rest
        and rest[0] != rest[1]
    )

for *items, in [set()]:
    result = result and items == []

for (da, db), in [({"u": 1, "v": 2},)]:
    result = result and da == "u" and db == "v"

else_seen = False
for *keys, in [{}]:
    result = result and keys == []
else:
    else_seen = True

result = result and else_seen
assert result
result
