first = 0
match [1, 2]:
    case [1, 2]:
        first = 1
    case _:
        first = 99

second = 0
match (3, 4):
    case (3, 5):
        second = 99
    case (3, 4):
        second = 2

third = 0
match []:
    case []:
        third = 3
    case _:
        third = 99

fourth = 0
match "ab":
    case ["a", "b"]:
        fourth = 99
    case _:
        fourth = 4

fifth = 0
fifth_alias = []
match [7, 8]:
    case [7, 8] as pair:
        fifth = 5
        fifth_alias = pair
    case _:
        fifth = 99

sixth = 0
match [0, True]:
    case [False, 1]:
        sixth = 99
    case [0, True]:
        sixth = 6

seventh = 0
match [1, 3]:
    case [1 | 2, 3]:
        seventh = 7
    case _:
        seventh = 99

result = (
    first == 1
    and second == 2
    and third == 3
    and fourth == 4
    and fifth == 5
    and fifth_alias == [7, 8]
    and sixth == 6
    and seventh == 7
)
assert result
result
