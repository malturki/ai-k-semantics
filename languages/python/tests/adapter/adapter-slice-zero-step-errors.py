list_expr = False
try:
    [1, 2, 3][::0]
except ValueError:
    list_expr = True

string_expr = False
try:
    "abc"[::False]
except ValueError:
    string_expr = True

range_expr = False
try:
    range(5)[::0]
except ValueError:
    range_expr = True

slice_object_expr = False
try:
    [1, 2, 3][slice(None, None, 0)]
except ValueError:
    slice_object_expr = True

assign_target = [1, 2, 3]
assign_error = False
try:
    assign_target[::0] = []
except ValueError:
    assign_error = assign_target == [1, 2, 3]

delete_target = [1, 2, 3]
delete_error = False
try:
    del delete_target[::0]
except ValueError:
    delete_error = delete_target == [1, 2, 3]

result = (
    list_expr
    and string_expr
    and range_expr
    and slice_object_expr
    and assign_error
    and delete_error
)
assert result
result
