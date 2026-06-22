head = 0
tail = 0
first = False
match [1, 2, 3, 4]:
    case [head, *_, tail]:
        first = head == 1 and tail == 4
    case _:
        first = False

start = 0
middle = []
end = 0
second = False
match [5, 6, 7, 8]:
    case [start, *middle, end]:
        second = start == 5 and middle == [6, 7] and end == 8
    case _:
        second = False

unchanged = "old"
third = False
match [1, 2, 3]:
    case [unchanged, *_, 4]:
        third = False
    case _:
        third = unchanged == "old"

guard_head = "old"
guard_tail = "old"
fourth = False
match [9, 10]:
    case [guard_head, *_, guard_tail] if False:
        fourth = False
    case _:
        fourth = guard_head == 9 and guard_tail == 10

tuple_head = 0
tuple_tail = 0
fifth = False
match (11, 12, 13):
    case (tuple_head, *_, tuple_tail):
        fifth = tuple_head == 11 and tuple_tail == 13
    case _:
        fifth = False

result = first and second and third and fourth and fifth
assert result
result
