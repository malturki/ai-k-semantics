def collect(first, *rest):
    return first == 1 and rest == (2, 3)

def empty(*items):
    return items == ()

result = collect(1, 2, 3)
result = result and empty()
assert result
result
