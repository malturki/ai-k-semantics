out = ""
for key in {}:
    out += key
else:
    out += "empty"

for key in {"a": 1}:
    out += key
else:
    out += "!"

for key in {"x": 1, "y": 2}:
    if key == "y":
        break
    out += key
else:
    out += "?"

out == "emptya!x"
