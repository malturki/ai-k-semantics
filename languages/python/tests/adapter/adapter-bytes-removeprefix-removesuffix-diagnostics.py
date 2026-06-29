data = b"abc"

errors_ok = True

try:
    data.removeprefix(97)
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removeprefix("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removeprefix((b"a",))
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removeprefix([97])
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removesuffix(99)
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removesuffix("c")
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removesuffix((b"c",))
except TypeError:
    pass
else:
    errors_ok = False

try:
    data.removesuffix([99])
except TypeError:
    pass
else:
    errors_ok = False

result = errors_ok and data == b"abc"
assert result
result
