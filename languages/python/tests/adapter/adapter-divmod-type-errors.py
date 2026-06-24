str_left = False
try:
    divmod("a", 1)
except TypeError:
    str_left = True

str_right = False
try:
    divmod(1, "a")
except TypeError:
    str_right = True

none_left = False
try:
    divmod(None, 1)
except TypeError:
    none_left = True

none_right = False
try:
    divmod(1, None)
except TypeError:
    none_right = True

complex_left = False
try:
    divmod(1 + 2j, 1)
except TypeError:
    complex_left = True

complex_right = False
try:
    divmod(1, 1 + 2j)
except TypeError:
    complex_right = True

list_left = False
try:
    divmod([], 1)
except TypeError:
    list_left = True

result = (
    str_left
    and str_right
    and none_left
    and none_right
    and complex_left
    and complex_right
    and list_left
)
assert result
result
