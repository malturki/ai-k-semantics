empty = set()
result = list(empty) == [] and tuple(empty) == ()

source = {3, 1, 2}
items = list(source)
pair = tuple(source)

result = result and len(items) == 3 and set(items) == source
result = result and len(pair) == 3 and set(pair) == source

assert result
result
