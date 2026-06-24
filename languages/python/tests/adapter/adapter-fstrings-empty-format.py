name = "Ada"
value = 7

result = f"{value:}:{name:}"
assert result == "7:Ada"

result = f"{value!s:}:{value!r:}:{value!a:}"
assert result == "7:7:7"

result = f"{name!r:}:{name!a:}"
assert result == "'Ada':'Ada'"

x = 0
result = f"{(x := 5):}:{x!r:}"
assert result == "5:5"

result == "5:5"
