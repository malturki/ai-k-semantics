name = "Ada"
value = 7

result = f"{value:04d}:{name:>5s}:{'python':.2s}"
assert result == "0007:  Ada:py"

result = f"{name!r:>7}:{value!s:0>3}:{value!a:^5}"
assert result == "  'Ada':007:  7  "

raised = False
try:
    f"{name:+s}"
except ValueError:
    raised = True

assert raised
raised
