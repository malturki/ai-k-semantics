selected = 0
match 2:
    case x if x == 1:
        selected = 10
    case x if x == 2:
        selected = x
    case _:
        selected = 99

skipped = "old"
match 1:
    case 2 if (skipped := "changed"):
        skipped = "bad"
    case 1 if True:
        skipped_ok = skipped == "old"
    case _:
        skipped_ok = False

after_false = "old"
match 3:
    case after_false if after_false == 4:
        after_false = "bad"
    case _:
        after_false_ok = after_false == 3

last_false = "old"
match 4:
    case last_false if False:
        last_false = "bad"
last_false_ok = last_false == 4

walrus_seen = False
match 5:
    case y if (walrus_seen := y == 5):
        walrus_ok = walrus_seen and y == 5
    case _:
        walrus_ok = False

def explode():
    raise ValueError

caught = False
guard_exception_name = "old"
try:
    match 6:
        case guard_exception_name if explode():
            caught = False
        case _:
            caught = False
except ValueError:
    caught = guard_exception_name == 6

result = selected == 2 and skipped_ok and after_false_ok and last_false_ok and walrus_ok and caught
assert result
result
