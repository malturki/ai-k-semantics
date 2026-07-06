result = True

import math, keyword as kw, importlib

from math import pi, tau as circle_tau, e

result = result and math.pi == pi
result = result and circle_tau == math.tau
result = result and e > 2.0
result = result and kw.iskeyword("for")
result = result and importlib.import_module("keyword") is kw

math.answer = 41
from math import answer, tau as again_tau

result = result and answer == 41
result = result and again_tau == math.tau

partial_failed = False
try:
    from math import pi as first_ok, never_there as never_alias
    result = False
except ImportError:
    partial_failed = True

never_missing = False
try:
    never_alias
    result = False
except NameError:
    never_missing = True

result = result and partial_failed
result = result and first_ok == math.pi
result = result and never_missing

result
