data = bytearray(b"banana")
empty = bytearray()

startswith_ok = (
    data.startswith(b"ban")
    and not data.startswith(b"ana")
    and data.startswith(bytearray(b"ban"))
    and data.startswith(memoryview(b"ban"))
    and data.startswith(b"")
    and empty.startswith(b"")
    and not empty.startswith(b"x")
    and data.startswith((b"ban", 1))
    and data.startswith((b"",))
    and data.startswith((memoryview(b"ban"),))
    and not data.startswith(())
)

endswith_ok = (
    data.endswith(b"ana")
    and not data.endswith(b"ban")
    and data.endswith(bytearray(b"ana"))
    and data.endswith(memoryview(b"ana"))
    and data.endswith(b"")
    and empty.endswith(b"")
    and not empty.endswith(b"x")
    and data.endswith((b"ana", 1))
    and data.endswith((b"",))
    and data.endswith((memoryview(b"ana"),))
    and not data.endswith(())
)

errors_ok = True
error_data = bytearray(b"abc")

try:
    error_data.startswith(97)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.startswith("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.startswith([97])
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.startswith((1, b"a"))
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.startswith((b"z", 1))
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.endswith(99)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.endswith("c")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.endswith([99])
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.endswith((1, b"c"))
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.endswith((b"z", 1))
except TypeError:
    pass
else:
    errors_ok = False

unchanged_ok = data == bytearray(b"banana") and error_data == bytearray(b"abc")

result = startswith_ok and endswith_ok and errors_ok and unchanged_ok
assert result
result
