first = False
rest = {}
match {"a": 1, "b": 2}:
    case {"a": 1, **rest}:
        first = rest == {"b": 2}
    case _:
        first = False

unchanged = "old"
second = False
match {"a": 1}:
    case {"b": 2, **unchanged}:
        second = False
    case _:
        second = unchanged == "old"

third = False
empty_rest = {"old": 1}
match {"a": 1}:
    case {"a": 1, **empty_rest}:
        third = empty_rest == {}
    case _:
        third = False

fourth = False
all_items = {}
match {"x": 1, "y": 2}:
    case {**all_items}:
        fourth = all_items == {"x": 1, "y": 2}
    case _:
        fourth = False

fifth = 0
match [("a", 1)]:
    case {"a": 1, **list_rest}:
        fifth = 99
    case _:
        fifth = 5

sixth = False
bool_rest = {}
match {False: "value", "keep": 1}:
    case {0: "value", **bool_rest}:
        sixth = bool_rest == {"keep": 1}
    case _:
        sixth = False

result = first and second and third and fourth and fifth == 5 and sixth
assert result
result
