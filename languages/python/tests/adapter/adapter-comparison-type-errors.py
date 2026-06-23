str_int = False
try:
    "a" < 1
except TypeError:
    str_int = True

int_str = False
try:
    1 <= "a"
except TypeError:
    int_str = True

list_tuple = False
try:
    [1] < (1,)
except TypeError:
    list_tuple = True

dict_order = False
try:
    {} < {}
except TypeError:
    dict_order = True

set_list = False
try:
    {1} > [1]
except TypeError:
    set_list = True

bytes_str = False
try:
    b"a" >= "a"
except TypeError:
    bytes_str = True

none_int = False
try:
    None < 0
except TypeError:
    none_int = True

complex_order = False
try:
    1j < 2j
except TypeError:
    complex_order = True

chained_first = False
try:
    1 < "x" < 3
except TypeError:
    chained_first = True

chained_second = False
try:
    1 < 2 < "x"
except TypeError:
    chained_second = True

chained_rhs_exception = False
try:
    0 < range(1, 5, 0) < 3
except ValueError:
    chained_rhs_exception = True

result = (
    str_int
    and int_str
    and list_tuple
    and dict_order
    and set_list
    and bytes_str
    and none_int
    and complex_order
    and chained_first
    and chained_second
    and chained_rhs_exception
)
assert result
result
