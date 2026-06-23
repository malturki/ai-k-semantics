xs = [[1, 2], {"a": 3}]
value = 9
xs[0][1] = value
xs[-1]["b"] = xs[0][1] + 1

d = {"items": [4, 5], "meta": {"x": 1}}
d["items"][0] = xs[1]["b"]
d["meta"]["y"] = d["items"][1]

del xs[0][0]
del xs[1]["a"]
del d["items"][-1]
del d["meta"]["x"]

result = (
    xs == [[9], {"b": 10}]
    and d == {"items": [10], "meta": {"y": 5}}
)
assert result
result
