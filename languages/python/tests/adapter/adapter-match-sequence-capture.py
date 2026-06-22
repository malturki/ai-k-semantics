first = False
left = 0
right = 0
match [1, 2]:
    case [left, right]:
        first = left == 1 and right == 2
    case _:
        first = False

unchanged = "old"
second = False
match [1, 2]:
    case [unchanged, 3]:
        second = False
    case _:
        second = unchanged == "old"

guard_name = "old"
third = False
match [4, 5]:
    case [guard_name, 5] if False:
        third = False
    case _:
        third = guard_name == 4

head = 0
fourth = False
match (1, 2, 3):
    case [head, 2, _]:
        fourth = head == 1
    case _:
        fourth = False

result = first and second and third and fourth
assert result
result
