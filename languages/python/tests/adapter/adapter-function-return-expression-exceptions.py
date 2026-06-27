def value():
    return 4 + 5


def fail_value():
    return 1 // 0


def pass_through():
    return fail_value()


direct_error = False
try:
    fail_value()
except ZeroDivisionError:
    direct_error = True

nested_error = False
try:
    pass_through()
except ZeroDivisionError:
    nested_error = True

result = value() == 9 and direct_error and nested_error
assert result
result
