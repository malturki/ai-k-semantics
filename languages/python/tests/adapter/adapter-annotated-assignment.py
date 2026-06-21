called = False

def mark():
    global called
    called = True
    return 0

x: mark() = 3
result = x == 3 and not called

y = 10
y: mark()
result = result and y == 10 and not called

z: missing_name = x + 4
result = result and z == 7 and not called

empty: other_missing_name
result = result and not called
result
