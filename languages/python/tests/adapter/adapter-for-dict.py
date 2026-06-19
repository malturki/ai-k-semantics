seen = ""
data = {"a": 1, "b": 2}
for key in data:
    seen += key

out = ""
for key in {"a": 1, "b": 2, "c": 3}:
    if key == "b":
        continue
    if key == "c":
        break
    out += key

seen == "ab" and out == "a"
