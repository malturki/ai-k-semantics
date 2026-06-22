first = 0
match {"a": 1, "b": 2}:
    case {"a": 1}:
        first = 1
    case _:
        first = 99

second = 0
match {"a": 1}:
    case {"b": 2}:
        second = 99
    case _:
        second = 2

third = 0
match {"a": 1}:
    case {"a": 2}:
        third = 99
    case {"a": 1}:
        third = 3

fourth = 0
match {}:
    case {}:
        fourth = 4
    case _:
        fourth = 99

fifth = 0
match [("a", 1)]:
    case {"a": 1}:
        fifth = 99
    case _:
        fifth = 5

sixth = False
alias = {}
match {"x": 5, "y": 6}:
    case {"x": 5} as got:
        sixth = got == {"x": 5, "y": 6}
        alias = got
    case _:
        sixth = False

seventh = 0
match {"tag": "beta"}:
    case {"tag": "alpha" | "beta"}:
        seventh = 7
    case _:
        seventh = 99

eighth = 0
match {False: "value"}:
    case {0: "value"}:
        eighth = 8
    case _:
        eighth = 99

result = (
    first == 1
    and second == 2
    and third == 3
    and fourth == 4
    and fifth == 5
    and sixth
    and alias == {"x": 5, "y": 6}
    and seventh == 7
    and eighth == 8
)
assert result
result
