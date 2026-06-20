value = 0
for item in [1, 2, 3]:
    try:
        if item == 2:
            break
        value += item
    finally:
        value += 10

result = value == 21

value = 0
for item in [1, 2, 3]:
    try:
        if item == 2:
            continue
        value += item
    finally:
        value += 10

result = result and value == 34


def break_overridden_by_finally_return():
    for item in [1]:
        try:
            break
        finally:
            return 7
    return 0


def continue_overridden_by_finally_return():
    for item in [1]:
        try:
            continue
        finally:
            return 8
    return 0


result = result and break_overridden_by_finally_return() == 7
result = result and continue_overridden_by_finally_return() == 8
assert result
result
