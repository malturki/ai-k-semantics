first = 0
match [1, 2, 3, 4]:
    case [1, *_, 4]:
        first = 1
    case _:
        first = 99

second = 0
match (1, 2):
    case (1, *_, 3):
        second = 99
    case (1, *_):
        second = 2

third = 0
match []:
    case [*_]:
        third = 3
    case _:
        third = 99

fourth = 0
match [1, 2]:
    case [1, *_, 2, 3]:
        fourth = 99
    case _:
        fourth = 4

fifth = 0
match "ab":
    case ["a", *_, "b"]:
        fifth = 99
    case _:
        fifth = 5

sixth = 0
sixth_alias = []
match [9, 8, 7]:
    case [9, *_, 7] as seq:
        sixth = 6
        sixth_alias = seq
    case _:
        sixth = 99

seventh = 0
match [0, 5, 3]:
    case [1 | 0, *_, 3]:
        seventh = 7
    case _:
        seventh = 99

result = (
    first == 1
    and second == 2
    and third == 3
    and fourth == 4
    and fifth == 5
    and sixth == 6
    and sixth_alias == [9, 8, 7]
    and seventh == 7
)
assert result
result
