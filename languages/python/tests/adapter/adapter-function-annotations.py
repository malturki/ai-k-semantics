called = False

def mark():
    global called
    called = True
    return 0

def identity(value: mark()) -> mark():
    return value

result = identity(7) == 7 and not called

def defaulted(value: mark() = 3) -> mark():
    return value + 1

result = result and defaulted() == 4 and not called

def multi(left: mark(), right: mark()) -> mark():
    return left + right

result = result and multi(2, 5) == 7 and not called

def unresolved(value: missing_name) -> other_missing_name:
    return value

result = result and unresolved(11) == 11 and not called
result
