name = "Ada"
value = 7

result = f"hello {name}: {value}"
assert result == "hello Ada: 7"

result = f"{True}:{False}:{None}:{...}"
assert result == "True:False:None:Ellipsis"

x = 0
result = f"{(x := 1)}-{(x := x + 2)}-{x}"
assert result == "1-3-3"

def inc(v):
    return v + 1

result = f"{inc(4)}"
assert result == "5"

raised = False
try:
    f"{1 / 0}"
except ZeroDivisionError:
    raised = True

assert raised
raised
