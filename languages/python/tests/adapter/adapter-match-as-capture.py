seq_item = 0
seq_whole = []
first = False
match [1, 2]:
    case [seq_item, 2] as seq_whole:
        first = seq_item == 1 and seq_whole == [1, 2]
    case _:
        first = False

unchanged = "old"
failed_whole = "whole"
second = False
match [1, 2]:
    case [unchanged, 3] as failed_whole:
        second = False
    case _:
        second = unchanged == "old" and failed_whole == "whole"

map_item = "old"
map_whole = "old"
third = False
match {"left": 4}:
    case {"left": map_item} as map_whole if False:
        third = False
    case _:
        third = map_item == 4 and map_whole == {"left": 4}

class_item = 0
class_whole = 0
fourth = False
match 5:
    case int(class_item) as class_whole:
        fourth = class_item == 5 and class_whole == 5
    case _:
        fourth = False

result = first and second and third and fourth
assert result
result
