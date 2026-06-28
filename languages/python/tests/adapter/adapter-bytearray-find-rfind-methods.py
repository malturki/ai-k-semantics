data = bytearray(b"banana")
bool_data = bytearray([0, 1, 1])
empty = bytearray()

find_ok = (
    data.find(97) == 1
    and data.find(120) == -1
    and bool_data.find(True) == 1
    and data.find(b"ana") == 1
    and data.find(bytearray(b"na")) == 2
    and data.find(memoryview(b"na")) == 2
    and data.find(b"") == 0
    and data.find(bytearray()) == 0
    and data.find(memoryview(b"")) == 0
    and data.find(b"zz") == -1
    and empty.find(b"") == 0
    and empty.find(1) == -1
)

rfind_ok = (
    data.rfind(97) == 5
    and data.rfind(120) == -1
    and bool_data.rfind(True) == 2
    and data.rfind(b"ana") == 3
    and data.rfind(bytearray(b"na")) == 4
    and data.rfind(memoryview(b"na")) == 4
    and data.rfind(b"") == 6
    and data.rfind(bytearray()) == 6
    and data.rfind(memoryview(b"")) == 6
    and data.rfind(b"zz") == -1
    and empty.rfind(b"") == 0
    and empty.rfind(1) == -1
)

errors_ok = True
error_data = bytearray(b"abc")

try:
    error_data.find(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.find(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.find(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.find("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind("a")
except TypeError:
    pass
else:
    errors_ok = False

unchanged_ok = data == bytearray(b"banana") and error_data == bytearray(b"abc")

result = find_ok and rfind_ok and errors_ok and unchanged_ok
assert result
result
