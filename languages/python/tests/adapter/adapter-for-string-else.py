out = ""
for ch in "":
    out += ch
else:
    out += "empty"

for ch in "ab":
    out += ch
else:
    out += "!"

for ch in "xy":
    if ch == "y":
        break
    out += ch
else:
    out += "?"

out == "emptyab!x"
