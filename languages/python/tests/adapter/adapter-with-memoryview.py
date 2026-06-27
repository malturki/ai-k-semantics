normal = False
after = False
with memoryview(b"abc"):
    normal = True
after = True

with_as = False
with memoryview(b"abc") as m:
    with_as = len(m) == 3 and isinstance(m, memoryview) and bool(m)

empty_truth = True
with memoryview(b"") as empty:
    empty_truth = bool(empty)

body_exception = False
try:
    with memoryview(b"x"):
        raise ValueError
except ValueError:
    body_exception = True

pre_entry_exception = False
body_skipped = True
try:
    with memoryview(1 // 0):
        body_skipped = False
except ZeroDivisionError:
    pre_entry_exception = True

bad_context = False
try:
    with 1:
        bad_context = False
except TypeError:
    bad_context = True

def returns_through_with():
    with memoryview(b"r"):
        return 7
    return 0

return_ok = returns_through_with() == 7

break_seen = 0
for item in [1, 2]:
    with memoryview(b"b"):
        break_seen = item
        break

continue_seen = 0
for item in [1, 2]:
    with memoryview(b"c"):
        continue_seen += item
        continue
    continue_seen += 100

result = (
    normal
    and after
    and with_as
    and not empty_truth
    and body_exception
    and pre_entry_exception
    and body_skipped
    and bad_context
    and return_ok
    and break_seen == 1
    and continue_seen == 3
)
assert result
result
