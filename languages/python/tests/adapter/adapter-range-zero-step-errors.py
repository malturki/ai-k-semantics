direct_zero = False
try:
    range(1, 5, 0)
except ValueError:
    direct_zero = True

bool_zero = False
try:
    range(1, 5, False)
except ValueError:
    bool_zero = True

for_header_zero = False
try:
    for item in range(1, 5, 0):
        pass
except ValueError:
    for_header_zero = True

for_body_zero = False
try:
    for item in range(1):
        range(1, 5, 0)
except ValueError:
    for_body_zero = True

while_condition_zero = False
try:
    while range(1, 5, 0):
        pass
except ValueError:
    while_condition_zero = True

while_body_zero = False
try:
    while True:
        range(1, 5, 0)
except ValueError:
    while_body_zero = True

result = (
    direct_zero
    and bool_zero
    and for_header_zero
    and for_body_zero
    and while_condition_zero
    and while_body_zero
)
assert result
result
