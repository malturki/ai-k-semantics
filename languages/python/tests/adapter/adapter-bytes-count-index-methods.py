data = b"banana"
bool_data = bytes([0, 1, 1])
empty = b""

count_a = data.count(97)
count_missing = data.count(120)
count_empty = empty.count(1)
count_bool = bool_data.count(True)

index_a = data.index(97)
index_n = data.index(110)
index_bool = bool_data.index(True)

queries_ok = (
    count_a == 3
    and count_missing == 0
    and count_empty == 0
    and count_bool == 2
    and index_a == 1
    and index_n == 2
    and index_bool == 1
)

errors_ok = True
error_data = b"ab"

try:
    error_data.count(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.count(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.count(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.count("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.index(120)
except ValueError:
    pass
else:
    errors_ok = False

try:
    empty.index(1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.index(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.index(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.index(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.index("a")
except TypeError:
    pass
else:
    errors_ok = False

errors_ok = errors_ok and error_data == b"ab" and empty == b""

result = queries_ok and errors_ok
assert result
result
