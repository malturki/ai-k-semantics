def collect(**kw):
    return kw["x"] + kw["not identifier"]

data = {"x": 1, "not identifier": 2}
result = collect(**data) == 3
result = result and collect(**{"x": 4}, **{"not identifier": 5}) == 9
assert result
result
