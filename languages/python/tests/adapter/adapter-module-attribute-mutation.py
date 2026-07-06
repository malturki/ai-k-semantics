result = True

import math
import math as math_alias

modules = [math, math_alias]
pair = (math, math_alias)
mapping = {"math": math, "alias": math_alias}
nested = [[math], {"alias": math_alias}]

math.answer = 41
result = result and math.answer == 41
result = result and math_alias.answer == 41
result = result and modules[0].answer == 41
result = result and modules[1].answer == 41
result = result and pair[0].answer == 41
result = result and pair[1].answer == 41
result = result and mapping["math"].answer == 41
result = result and mapping["alias"].answer == 41
result = result and nested[0][0].answer == 41
result = result and nested[1]["alias"].answer == 41

setattr(modules[1], "answer", 42)
result = result and math.answer == 42
result = result and math_alias.answer == 42
result = result and modules[0].answer == 42
result = result and modules[1].answer == 42
result = result and pair[0].answer == 42
result = result and pair[1].answer == 42
result = result and mapping["math"].answer == 42
result = result and mapping["alias"].answer == 42
result = result and nested[0][0].answer == 42
result = result and nested[1]["alias"].answer == 42

del pair[0].answer
result = result and not hasattr(math, "answer")
result = result and not hasattr(math_alias, "answer")
result = result and not hasattr(modules[0], "answer")
result = result and not hasattr(modules[1], "answer")
result = result and not hasattr(pair[0], "answer")
result = result and not hasattr(pair[1], "answer")
result = result and not hasattr(mapping["math"], "answer")
result = result and not hasattr(mapping["alias"], "answer")
result = result and not hasattr(nested[0][0], "answer")
result = result and not hasattr(nested[1]["alias"], "answer")

setattr(nested[1]["alias"], "dynamic", 99)
result = result and getattr(math, "dynamic") == 99
result = result and getattr(math_alias, "dynamic") == 99
result = result and getattr(modules[0], "dynamic") == 99
result = result and getattr(modules[1], "dynamic") == 99
result = result and getattr(pair[0], "dynamic") == 99
result = result and getattr(pair[1], "dynamic") == 99
result = result and getattr(mapping["math"], "dynamic") == 99
result = result and getattr(mapping["alias"], "dynamic") == 99
result = result and getattr(nested[0][0], "dynamic") == 99
result = result and getattr(nested[1]["alias"], "dynamic") == 99

delattr(math_alias, "dynamic")
result = result and getattr(math, "dynamic", 17) == 17
result = result and getattr(math_alias, "dynamic", 17) == 17
result = result and getattr(modules[0], "dynamic", 17) == 17
result = result and getattr(modules[1], "dynamic", 17) == 17
result = result and getattr(pair[0], "dynamic", 17) == 17
result = result and getattr(pair[1], "dynamic", 17) == 17
result = result and getattr(mapping["math"], "dynamic", 17) == 17
result = result and getattr(mapping["alias"], "dynamic", 17) == 17
result = result and getattr(nested[0][0], "dynamic", 17) == 17
result = result and getattr(nested[1]["alias"], "dynamic", 17) == 17

try:
    del math_alias.dynamic
    result = False
except AttributeError:
    result = result and True

math.pi = 3
result = result and math.pi == 3
result = result and math_alias.pi == 3
result = result and modules[0].pi == 3
delattr(modules[0], "pi")
result = result and not hasattr(math, "pi")
result = result and not hasattr(math_alias, "pi")
result = result and not hasattr(modules[0], "pi")

result
