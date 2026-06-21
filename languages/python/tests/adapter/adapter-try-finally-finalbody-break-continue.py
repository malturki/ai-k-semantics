value = 0
for item in [1, 2, 3]:
    try:
        value += item
    finally:
        break

result = value == 1

value = 0
for item in [1, 2, 3]:
    try:
        value += item
    finally:
        if item < 3:
            continue
    value += 10

result = result and value == 16

value = 0
for item in [1, 2, 3]:
    try:
        if item == 1:
            continue
        value += item
    finally:
        break

result = result and value == 0

value = 0
for item in [1, 2, 3]:
    try:
        break
    finally:
        value += item
        if item < 3:
            continue
    value += 10

result = result and value == 6
assert result
result
