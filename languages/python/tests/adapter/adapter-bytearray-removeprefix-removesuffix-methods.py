data = bytearray(b"banana")
empty = bytearray()
prefix_bytes = b"ban"
suffix_bytes = b"ana"
prefix_bytearray = bytearray(b"ban")
suffix_bytearray = bytearray(b"ana")
prefix_view = memoryview(b"ban")
suffix_view = memoryview(b"ana")

removeprefix_ok = (
    data.removeprefix(prefix_bytes) == bytearray(b"ana")
    and data.removeprefix(b"ana") == bytearray(b"banana")
    and data.removeprefix(prefix_bytearray) == bytearray(b"ana")
    and data.removeprefix(prefix_view) == bytearray(b"ana")
    and data.removeprefix(b"") == bytearray(b"banana")
    and data.removeprefix(b"banana") == bytearray()
    and empty.removeprefix(b"") == bytearray()
    and empty.removeprefix(b"x") == bytearray()
)

removesuffix_ok = (
    data.removesuffix(suffix_bytes) == bytearray(b"ban")
    and data.removesuffix(b"ban") == bytearray(b"banana")
    and data.removesuffix(suffix_bytearray) == bytearray(b"ban")
    and data.removesuffix(suffix_view) == bytearray(b"ban")
    and data.removesuffix(b"") == bytearray(b"banana")
    and data.removesuffix(b"banana") == bytearray()
    and empty.removesuffix(b"") == bytearray()
    and empty.removesuffix(b"x") == bytearray()
)

errors_ok = True
error_data = bytearray(b"abc")

try:
    error_data.removeprefix(97)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removeprefix("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removeprefix((b"a",))
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removeprefix([97])
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removesuffix(99)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removesuffix("c")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removesuffix((b"c",))
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.removesuffix([99])
except TypeError:
    pass
else:
    errors_ok = False

unchanged_ok = data == bytearray(b"banana") and error_data == bytearray(b"abc")

result = removeprefix_ok and removesuffix_ok and errors_ok and unchanged_ok
assert result
result
