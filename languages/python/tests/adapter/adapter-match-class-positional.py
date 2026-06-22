def tag(value):
    match value:
        case bool(True):
            return "bool-true"
        case int(0 | 1):
            return "small-int"
        case float(1.5):
            return "float"
        case str("x"):
            return "str"
        case bytes(b"x"):
            return "bytes"
        case list([1, 2]):
            return "list"
        case tuple((1, 2)):
            return "tuple"
        case dict({"a": 1}):
            return "dict"
        case set(_):
            return "set"
        case _:
            return "other"

direct = (
    tag(True) == "bool-true"
    and tag(1) == "small-int"
    and tag(1.5) == "float"
    and tag("x") == "str"
    and tag(b"x") == "bytes"
    and tag([1, 2]) == "list"
    and tag((1, 2)) == "tuple"
    and tag({"a": 1}) == "dict"
    and tag({1}) == "set"
    and tag([1]) == "other"
)

bool_as_int = False
match True:
    case int(1):
        bool_as_int = True
    case _:
        bool_as_int = False

class_check_first = False
match 1.0:
    case int(1.0):
        class_check_first = False
    case float(1.0):
        class_check_first = True
    case _:
        class_check_first = False

guarded = False
match 3:
    case int(3) if False:
        guarded = False
    case int(3):
        guarded = True
    case _:
        guarded = False

result = direct and bool_as_int and class_check_first and guarded
assert result
result
