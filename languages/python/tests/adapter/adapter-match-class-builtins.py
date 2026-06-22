def tag(value):
    match value:
        case bool():
            return "bool"
        case int():
            return "int"
        case float():
            return "float"
        case complex():
            return "complex"
        case str():
            return "str"
        case bytes():
            return "bytes"
        case list():
            return "list"
        case tuple():
            return "tuple"
        case dict():
            return "dict"
        case set():
            return "set"
        case range():
            return "range"
        case slice():
            return "slice"
        case _:
            return "other"

direct = (
    tag(True) == "bool"
    and tag(1) == "int"
    and tag(1.5) == "float"
    and tag(1j) == "complex"
    and tag("x") == "str"
    and tag(b"x") == "bytes"
    and tag([1]) == "list"
    and tag((1,)) == "tuple"
    and tag({"a": 1}) == "dict"
    and tag({1}) == "set"
    and tag(range(3)) == "range"
    and tag(slice(1, 2)) == "slice"
    and tag(None) == "other"
)

bool_as_int = False
match True:
    case int():
        bool_as_int = True
    case _:
        bool_as_int = False

nested = False
match [1, "x"]:
    case [int(), str()]:
        nested = True
    case _:
        nested = False

or_pattern = False
match b"x":
    case str() | bytes():
        or_pattern = True
    case _:
        or_pattern = False

guarded = False
match 3:
    case float() if True:
        guarded = False
    case int() if False:
        guarded = False
    case int():
        guarded = True
    case _:
        guarded = False

result = direct and bool_as_int and nested and or_pattern and guarded
assert result
result
