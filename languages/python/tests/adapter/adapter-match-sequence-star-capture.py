first = False
middle = []
match [1, 2, 3, 4]:
    case [1, *middle, 4]:
        first = middle == [2, 3]
    case _:
        first = False

second = False
tail = []
match (1, 2, 3):
    case (1, *tail):
        second = tail == [2, 3]
    case _:
        second = False

third = False
empty = [99]
match []:
    case [*empty]:
        third = empty == []
    case _:
        third = False

fourth = 0
match [1, 2]:
    case [1, *too_short, 2, 3]:
        fourth = 99
    case [1, *just_middle]:
        fourth = 4

fifth = False
between = []
match [False, 7, 0]:
    case [False, *between, 0]:
        fifth = between == [7]
    case _:
        fifth = False

result = first and second and third and fourth == 4 and just_middle == [2] and fifth
assert result
result
