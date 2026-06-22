seq_value = 0
first = False
match [9, 1]:
    case [seq_value, 0] | [seq_value, 1]:
        first = seq_value == 9
    case _:
        first = False

unchanged = "old"
second = False
match [9, 2]:
    case [unchanged, 0] | [unchanged, 1]:
        second = False
    case _:
        second = unchanged == "old"

guard_name = "old"
third = False
match [4, 1]:
    case [guard_name, 0] | [guard_name, 1] if False:
        third = False
    case _:
        third = guard_name == 4

number = 0.0
fourth = False
match 1.5:
    case int(number) | float(number):
        fourth = number == 1.5
    case _:
        fourth = False

mapping_value = 0
fifth = False
match {"left": 6, "tag": 1}:
    case {"left": mapping_value, "tag": 0} | {"left": mapping_value, "tag": 1}:
        fifth = mapping_value == 6
    case _:
        fifth = False

result = first and second and third and fourth and fifth
assert result
result
