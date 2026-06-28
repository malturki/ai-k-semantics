data = bytearray(b"a:b:c")
plain = bytearray(b"abc")
prefix = bytearray(b"abc")
suffix = bytearray(b"abc")
double = bytearray(b"ab<>cd<>ef")
empty = bytearray()

partition_ok = (
    data.partition(b":") == (bytearray(b"a"), bytearray(b":"), bytearray(b"b:c"))
    and data.partition(bytearray(b":")) == (bytearray(b"a"), bytearray(b":"), bytearray(b"b:c"))
    and prefix.partition(b"ab") == (bytearray(), bytearray(b"ab"), bytearray(b"c"))
    and double.partition(b"<>") == (bytearray(b"ab"), bytearray(b"<>"), bytearray(b"cd<>ef"))
)

rpartition_ok = (
    data.rpartition(b":") == (bytearray(b"a:b"), bytearray(b":"), bytearray(b"c"))
    and data.rpartition(memoryview(b":")) == (bytearray(b"a:b"), bytearray(b":"), bytearray(b"c"))
    and suffix.rpartition(b"bc") == (bytearray(b"a"), bytearray(b"bc"), bytearray())
    and double.rpartition(bytearray(b"<>")) == (bytearray(b"ab<>cd"), bytearray(b"<>"), bytearray(b"ef"))
)

not_found_ok = (
    plain.partition(b":") == (bytearray(b"abc"), bytearray(), bytearray())
    and plain.rpartition(b":") == (bytearray(), bytearray(), bytearray(b"abc"))
    and empty.partition(b"x") == (bytearray(), bytearray(), bytearray())
    and empty.rpartition(b"x") == (bytearray(), bytearray(), bytearray())
)

value_error_ok = True
try:
    data.partition(b"")
    value_error_ok = False
except ValueError:
    pass

try:
    data.rpartition(bytearray())
    value_error_ok = False
except ValueError:
    pass

type_error_ok = True
try:
    data.partition(97)
    type_error_ok = False
except TypeError:
    pass

try:
    data.rpartition("a")
    type_error_ok = False
except TypeError:
    pass

try:
    data.partition([97])
    type_error_ok = False
except TypeError:
    pass

unchanged_ok = data == bytearray(b"a:b:c") and plain == bytearray(b"abc") and double == bytearray(b"ab<>cd<>ef")

result = partition_ok and rpartition_ok and not_found_ok and value_error_ok and type_error_ok and unchanged_ok
assert result
result
