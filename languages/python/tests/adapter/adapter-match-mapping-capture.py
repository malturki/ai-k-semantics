first = False
left = 0
right = 0
match {"left": 1, "right": 2}:
    case {"left": left, "right": right}:
        first = left == 1 and right == 2
    case _:
        first = False

unchanged = "old"
second = False
match {"left": 1, "right": 2}:
    case {"left": unchanged, "right": 3}:
        second = False
    case _:
        second = unchanged == "old"

guard_name = "old"
third = False
match {"left": 4}:
    case {"left": guard_name} if False:
        third = False
    case _:
        third = guard_name == 4

value = 0
rest = {}
fourth = False
match {"left": 5, "right": 6, "extra": 7}:
    case {"left": value, **rest}:
        fourth = value == 5 and rest == {"right": 6, "extra": 7}
    case _:
        fourth = False

result = first and second and third and fourth
assert result
result
