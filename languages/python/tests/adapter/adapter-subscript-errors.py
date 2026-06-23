string_high = False
try:
    "a"[1]
except IndexError:
    string_high = True

string_low = False
try:
    "a"[-2]
except IndexError:
    string_low = True

bytes_empty = False
try:
    b""[0]
except IndexError:
    bytes_empty = True

list_high = False
try:
    [1, 2][2]
except IndexError:
    list_high = True

list_low = False
try:
    [1, 2][-3]
except IndexError:
    list_low = True

tuple_high = False
try:
    (1, 2)[2]
except IndexError:
    tuple_high = True

range_high = False
try:
    range(2)[2]
except IndexError:
    range_high = True

range_empty = False
try:
    range(0)[0]
except IndexError:
    range_empty = True

dict_missing_string = False
try:
    {"x": 1}["y"]
except KeyError:
    dict_missing_string = True

dict_missing_int = False
try:
    {}[0]
except KeyError:
    dict_missing_int = True

result = (
    string_high
    and string_low
    and bytes_empty
    and list_high
    and list_low
    and tuple_high
    and range_high
    and range_empty
    and dict_missing_string
    and dict_missing_int
)
assert result
result
