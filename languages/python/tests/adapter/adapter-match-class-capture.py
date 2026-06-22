number = 0
first = False
match 7:
    case int(number):
        first = number == 7
    case _:
        first = False

unchanged = "old"
second = False
match "not an int":
    case int(unchanged):
        second = False
    case _:
        second = unchanged == "old"

guard_name = "old"
third = False
match 9:
    case int(guard_name) if False:
        third = False
    case _:
        third = guard_name == 9

items = []
fourth = False
match [1, 2]:
    case list(items):
        fourth = items == [1, 2]
    case _:
        fourth = False

result = first and second and third and fourth
assert result
result
