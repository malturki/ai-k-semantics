pos = float("inf")
neg = float("-inf")
nan = float("nan")

result = format(pos, ".,f") == "inf"
result = result and format(neg, "8_.3_f") == "    -inf"

width_group_dot_error = False
try:
    format(pos, ",.f")
except ValueError:
    width_group_dot_error = True

both_grouping_n_error = False
try:
    format(nan, ",.,n")
except ValueError:
    both_grouping_n_error = True

result = result and width_group_dot_error and both_grouping_n_error

assert result
result
