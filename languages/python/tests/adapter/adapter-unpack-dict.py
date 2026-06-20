a, b = {"x": 1, "y": 2}
result = a == "x" and b == "y"

first, *rest = {"p": 1, "q": 2, "r": 3}
result = result and first == "p" and rest == ["q", "r"]

((ka, kb),) = {(1, 2): "pair"}
result = result and ka == 1 and kb == 2

*empty_keys, = {}
result = result and empty_keys == []

assert result
result
