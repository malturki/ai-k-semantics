outer = {}
head = 0
middle = []
tail = 0
rest = {}
first = False
match {"payload": [1, 2, 3, 4], "keep": 5}:
    case {"payload": [head, *middle, tail], **rest} as outer:
        first = (
            head == 1
            and middle == [2, 3]
            and tail == 4
            and rest == {"keep": 5}
            and outer == {"payload": [1, 2, 3, 4], "keep": 5}
        )
    case _:
        first = False

inner_value = 0
inner_rest = {}
second = False
match [{"a": 6, "b": 7}]:
    case [{"a": inner_value, **inner_rest}]:
        second = inner_value == 6 and inner_rest == {"b": 7}
    case _:
        second = False

as_head = 0
as_mid = []
as_whole = []
third = False
match [[8, 9, 10]]:
    case [[as_head, *as_mid, 10] as as_whole]:
        third = as_head == 8 and as_mid == [9] and as_whole == [8, 9, 10]
    case _:
        third = False

or_value = 0
fourth = False
match [{"tag": 1, "value": [11, 12]}]:
    case [{"tag": 0, "value": [or_value]}] | [{"tag": 1, "value": [or_value, 12]}]:
        fourth = or_value == 11
    case _:
        fourth = False

class_value = 0
fifth = False
match {"n": 16}:
    case {"n": int(class_value)}:
        fifth = class_value == 16
    case _:
        fifth = False

unchanged = "old"
unchanged_rest = "old-rest"
sixth = False
match [{"a": [1, 2], "b": 3}]:
    case [{"a": [unchanged, 4], **unchanged_rest}]:
        sixth = False
    case _:
        sixth = unchanged == "old" and unchanged_rest == "old-rest"

guard_value = "old"
guard_middle = []
guard_rest = {}
seventh = False
match {"a": [13, 14], "b": 15}:
    case {"a": [guard_value, *guard_middle], **guard_rest} if False:
        seventh = False
    case _:
        seventh = guard_value == 13 and guard_middle == [14] and guard_rest == {"b": 15}

result = first and second and third and fourth and fifth and sixth and seventh
assert result
result
