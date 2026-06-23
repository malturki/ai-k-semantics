short_rhs = [0, 1, 2, 3]
caught_short = False
try:
    short_rhs[::2] = [9]
except ValueError:
    caught_short = short_rhs == [0, 1, 2, 3]

long_rhs = [0, 1, 2, 3]
caught_long = False
try:
    long_rhs[::2] = (7, 8, 9)
except ValueError:
    caught_long = long_rhs == [0, 1, 2, 3]

empty_rhs = [0, 1, 2, 3]
caught_empty = False
try:
    empty_rhs[::2] = []
except ValueError:
    caught_empty = empty_rhs == [0, 1, 2, 3]

string_rhs = [0, 1, 2, 3]
caught_string = False
try:
    string_rhs[::2] = "abc"
except ValueError:
    caught_string = string_rhs == [0, 1, 2, 3]

negative_step = [0, 1, 2, 3, 4, 5]
caught_negative = False
try:
    negative_step[5:0:-2] = range(2)
except ValueError:
    caught_negative = negative_step == [0, 1, 2, 3, 4, 5]

empty_target = []
caught_empty_target = False
try:
    empty_target[::2] = [1]
except ValueError:
    caught_empty_target = empty_target == []

result = (
    caught_short
    and caught_long
    and caught_empty
    and caught_string
    and caught_negative
    and caught_empty_target
)
assert result
result
