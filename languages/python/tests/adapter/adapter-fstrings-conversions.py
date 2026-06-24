name = "Ada"
value = 7

result = f"{value!s}:{value!r}:{value!a}"
assert result == "7:7:7"

result = f"{name!r}:{name!a}"
assert result == "'Ada':'Ada'"

result = f"{value=}:{name=!r}"
assert result == "value=7:name='Ada'"

x = 0
result = f"{(x := 4)!r}:{x=}"
assert result == "4:x=4"

result == "4:x=4"
