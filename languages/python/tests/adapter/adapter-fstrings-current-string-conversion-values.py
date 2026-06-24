values = [1, "x", b"AZ"]
pair = (1,)
mapping = {"a": 1}
empty_set = set()
rng = range(2)
slc = slice(1, 2)
pos_inf = float("inf")

result = f"{values}:{pair}:{mapping}:{empty_set}:{rng}:{slc}:{pos_inf}"
assert result == "[1, 'x', b'AZ']:(1,):{'a': 1}:set():range(0, 2):slice(1, 2, None):inf"

assert f"{values!s}:{rng!r}:{slc!a}" == "[1, 'x', b'AZ']:range(0, 2):slice(1, 2, None)"

result == "[1, 'x', b'AZ']:(1,):{'a': 1}:set():range(0, 2):slice(1, 2, None):inf"
