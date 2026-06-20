value = 0
try:
    value = 1
    value += 2
finally:
    value *= 10

result = value == 30

try:
    pass
finally:
    value += 5

result = result and value == 35

try:
    for item in [1, 2, 3]:
        value += item
finally:
    value += 100

result = result and value == 141
assert result
result
