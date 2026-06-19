out = ""
for ch in "abcd":
    if ch == "b":
        continue
    if ch == "d":
        break
    out += ch

out == "ac"
