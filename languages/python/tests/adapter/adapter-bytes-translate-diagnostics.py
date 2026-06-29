identity = bytes.maketrans(b"", b"")
data = b"abc"

short_table = False
try:
    data.translate(b"x")
except ValueError:
    short_table = True

short_table_before_delete = False
try:
    data.translate(b"x", 1)
except ValueError:
    short_table_before_delete = True

table_type_error = False
try:
    data.translate("x", b"a")
except TypeError:
    table_type_error = True

delete_type_error = False
try:
    data.translate(identity, 123)
except TypeError:
    delete_type_error = True

maketrans_value_error = False
try:
    bytes.maketrans(b"a", b"xy")
except ValueError:
    maketrans_value_error = True

maketrans_from_type_error = False
try:
    bytes.maketrans("a", b"x")
except TypeError:
    maketrans_from_type_error = True

maketrans_to_type_error = False
try:
    bytearray.maketrans(b"a", "x")
except TypeError:
    maketrans_to_type_error = True

result = short_table and short_table_before_delete and table_type_error
result = result and delete_type_error and maketrans_value_error
result = result and maketrans_from_type_error and maketrans_to_type_error

assert result
result
