result = bool() is False and bool(False) is False and bool(True) is True
result = result and bool(0) is False and bool(1) is True and bool(-1) is True
result = result and bool("") is False and bool("x") is True
result = result and bool([]) is False and bool([0]) is True
result = result and bool(()) is False and bool((0,)) is True
result = result and bool({}) is False and bool({"x": 1}) is True
result = result and bool(set()) is False and bool({1}) is True
result = result and bool(range(0)) is False and bool(range(1)) is True
assert result
result
