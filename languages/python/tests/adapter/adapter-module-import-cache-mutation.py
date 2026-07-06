result = True

import importlib
import math as math_alias

math_alias.pi = 3
math_alias.answer = 41

import math
result = result and math is math_alias
result = result and math.pi == 3
result = result and math.answer == 41

from math import pi as imported_pi
result = result and imported_pi == 3

again = importlib.import_module("math")
result = result and again is math
result = result and again.pi == 3
result = result and again.answer == 41

again_with_package = importlib.import_module("math", None)
result = result and again_with_package is math
result = result and again_with_package.answer == 41

setattr(again, "later", 99)
import math as later_math
result = result and later_math is math
result = result and later_math.later == 99
result = result and math_alias.later == 99

del math_alias.pi
import math as no_pi
result = result and no_pi is math
result = result and not hasattr(no_pi, "pi")
result = result and not hasattr(importlib.import_module("math"), "pi")

missing_from = False
try:
    from math import pi as deleted_pi
    result = False
except ImportError:
    missing_from = True

result = result and missing_from

result
