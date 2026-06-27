entered = False
after = False
with memoryview(b"a") as left, memoryview(b"bc") as right:
    entered = (
        len(left) == 1
        and len(right) == 2
        and isinstance(left, memoryview)
        and isinstance(right, memoryview)
        and bool(left)
        and bool(right)
    )
after = True

body_exception = False
try:
    with memoryview(b"x"), memoryview(b"y"):
        raise ValueError
except ValueError:
    body_exception = True

second_expr_exception = False
second_body_skipped = True
try:
    with memoryview(b"x"), memoryview(1 // 0):
        second_body_skipped = False
except ZeroDivisionError:
    second_expr_exception = True

second_bad_context = False
bad_body_skipped = True
try:
    with memoryview(b"x"), 1:
        bad_body_skipped = False
except TypeError:
    second_bad_context = True

def returns_through_multiple_with():
    with memoryview(b"r"), memoryview(b"s"):
        return 11
    return 0

return_ok = returns_through_multiple_with() == 11

break_seen = 0
for item in [1, 2]:
    with memoryview(b"b"), memoryview(b"c"):
        break_seen = item
        break

continue_seen = 0
for item in [1, 2]:
    with memoryview(b"b"), memoryview(b"c"):
        continue_seen += item
        continue
    continue_seen += 100

result = (
    entered
    and after
    and body_exception
    and second_expr_exception
    and second_body_skipped
    and second_bad_context
    and bad_body_skipped
    and return_ok
    and break_seen == 1
    and continue_seen == 3
)
assert result
result
