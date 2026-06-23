negate = lambda x: 0 - x

result = min([3, 1, 2], default=99, key=negate) == 3
result = result and max([3, 1, 2], default=-1, key=negate) == 1
result = result and min((3, 1, 2), key=negate, default=99) == 3
result = result and max(range(1, 4), key=negate, default=-1) == 1
result = result and min([3, 1, 2], default=99, key=None) == 1
result = result and max({1: "a", 4: "b", 2: "c"}, key=None, default=-1) == 4

marker = 0
result = result and min([], default=(marker := 7), key=(marker := 8)) == 7
result = result and marker == 8

marker = 0
result = result and max((), key=(marker := 8), default=(marker := 7)) == 7
result = result and marker == 7

marker = 0
min_args_default_key_error = False
try:
    min(1, 2, default=(marker := 7), key=(marker := 8))
except TypeError:
    min_args_default_key_error = True
result = result and min_args_default_key_error and marker == 8

marker = 0
max_args_key_default_error = False
try:
    max(1, 2, key=(marker := 8), default=(marker := 7))
except TypeError:
    max_args_key_default_error = True
result = result and max_args_key_default_error and marker == 7

assert result
result
