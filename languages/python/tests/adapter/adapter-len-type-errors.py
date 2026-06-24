int_len = False
try:
    len(1)
except TypeError:
    int_len = True

bool_len = False
try:
    len(True)
except TypeError:
    bool_len = True

float_len = False
try:
    len(1.0)
except TypeError:
    float_len = True

none_len = False
try:
    len(None)
except TypeError:
    none_len = True

ellipsis_len = False
try:
    len(...)
except TypeError:
    ellipsis_len = True

complex_len = False
try:
    len(1j)
except TypeError:
    complex_len = True

slice_len = False
try:
    len(slice(1))
except TypeError:
    slice_len = True

lambda_len = False
try:
    len(lambda x: x)
except TypeError:
    lambda_len = True

result = (
    int_len
    and bool_len
    and float_len
    and none_len
    and ellipsis_len
    and complex_len
    and slice_len
    and lambda_len
)
assert result
result
