string_repeat_float = False
try:
    "a" * 1.0
except TypeError:
    string_repeat_float = True

float_repeat_string = False
try:
    1.0 * "a"
except TypeError:
    float_repeat_string = True

bytes_repeat_none = False
try:
    b"a" * None
except TypeError:
    bytes_repeat_none = True

none_repeat_bytes = False
try:
    None * b"a"
except TypeError:
    none_repeat_bytes = True

list_repeat_string = False
try:
    [1] * "x"
except TypeError:
    list_repeat_string = True

string_repeat_list = False
try:
    "x" * [1]
except TypeError:
    string_repeat_list = True

tuple_repeat_list = False
try:
    (1,) * []
except TypeError:
    tuple_repeat_list = True

empty_list_repeat_tuple = False
try:
    [] * (1,)
except TypeError:
    empty_list_repeat_tuple = True

string_concat_int = False
try:
    "a" + 1
except TypeError:
    string_concat_int = True

int_concat_string = False
try:
    1 + "a"
except TypeError:
    int_concat_string = True

bytes_concat_string = False
try:
    b"a" + "b"
except TypeError:
    bytes_concat_string = True

string_concat_bytes = False
try:
    "a" + b"b"
except TypeError:
    string_concat_bytes = True

list_concat_tuple = False
try:
    [1] + (2,)
except TypeError:
    list_concat_tuple = True

tuple_concat_list = False
try:
    (1,) + [2]
except TypeError:
    tuple_concat_list = True

empty_list_concat_tuple = False
try:
    [] + ()
except TypeError:
    empty_list_concat_tuple = True

empty_tuple_concat_list = False
try:
    () + []
except TypeError:
    empty_tuple_concat_list = True

result = (
    string_repeat_float
    and float_repeat_string
    and bytes_repeat_none
    and none_repeat_bytes
    and list_repeat_string
    and string_repeat_list
    and tuple_repeat_list
    and empty_list_repeat_tuple
    and string_concat_int
    and int_concat_string
    and bytes_concat_string
    and string_concat_bytes
    and list_concat_tuple
    and tuple_concat_list
    and empty_list_concat_tuple
    and empty_tuple_concat_list
)
assert result
result
