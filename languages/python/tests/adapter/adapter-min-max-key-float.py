values = [3, 1, 2]
result = min(values, key=lambda x: x / 2) == 1
result = result and max(values, key=lambda x: x / 2) == 3

result = result and min(3, 1, 2, key=lambda x: x / 2) == 1
result = result and max(3, 1, 2, key=lambda x: x / 2) == 3

result = result and min(values, default=99, key=lambda x: x / 2) == 1
result = result and max(values, key=lambda x: x / 2, default=99) == 3

result = result and min(["b", "a"], key=lambda x: 0.5) == "b"
result = result and max(["b", "a"], key=lambda x: 0.5) == "b"

assert result
result
