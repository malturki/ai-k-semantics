pos_inf_default = False
try:
    round(float("inf"))
except OverflowError:
    pos_inf_default = True

neg_inf_default = False
try:
    round(float("-inf"))
except OverflowError:
    neg_inf_default = True

nan_default = False
try:
    round(float("nan"))
except ValueError:
    nan_default = True

pos_inf_none = False
try:
    round(float("inf"), None)
except OverflowError:
    pos_inf_none = True

neg_inf_none = False
try:
    round(float("-inf"), None)
except OverflowError:
    neg_inf_none = True

nan_none = False
try:
    round(float("nan"), None)
except ValueError:
    nan_none = True

result = pos_inf_default and neg_inf_default and nan_default
result = result and pos_inf_none and neg_inf_none and nan_none
result = result and round(float("inf"), 2) == float("inf")
result = result and round(float("-inf"), 2) == float("-inf")

rounded_nan = round(float("nan"), 2)
result = result and rounded_nan != rounded_nan

assert result
result
