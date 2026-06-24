str_value = False
try:
    abs("a")
except TypeError:
    str_value = True

none_value = False
try:
    abs(None)
except TypeError:
    none_value = True

list_value = False
try:
    abs([])
except TypeError:
    list_value = True

tuple_value = False
try:
    abs(())
except TypeError:
    tuple_value = True

dict_value = False
try:
    abs({})
except TypeError:
    dict_value = True

set_value = False
try:
    abs(set())
except TypeError:
    set_value = True

bytes_value = False
try:
    abs(b"a")
except TypeError:
    bytes_value = True

ellipsis_value = False
try:
    abs(...)
except TypeError:
    ellipsis_value = True

result = (
    str_value
    and none_value
    and list_value
    and tuple_value
    and dict_value
    and set_value
    and bytes_value
    and ellipsis_value
)
assert result
result
