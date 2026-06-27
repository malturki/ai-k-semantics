tuple_target = False
with memoryview(b"ab") as (left, right):
    tuple_target = left == 97 and right == 98

list_target = False
with memoryview(b"xy") as [x_byte, y_byte]:
    list_target = x_byte == 120 and y_byte == 121

star_target = False
with memoryview(b"abc") as (head, *tail):
    star_target = head == 97 and tail == [98, 99]

multi_target = False
with memoryview(b"z") as first, memoryview(b"cd") as (c_byte, d_byte):
    multi_target = isinstance(first, memoryview) and c_byte == 99 and d_byte == 100

arity_error = False
arity_body_skipped = True
try:
    with memoryview(b"a") as (one, two):
        arity_body_skipped = False
except ValueError:
    arity_error = True

def returns_after_target_bind():
    with memoryview(b"q") as (q_byte,):
        return q_byte
    return 0

return_ok = returns_after_target_bind() == 113

result = (
    tuple_target
    and list_target
    and star_target
    and multi_target
    and arity_error
    and arity_body_skipped
    and return_ok
)
assert result
result
