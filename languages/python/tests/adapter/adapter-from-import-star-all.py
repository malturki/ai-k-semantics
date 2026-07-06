result = True

import keyword

keyword.__all__ = ["kwlist"]
from keyword import *

result = result and "False" in kwlist

iskeyword_missing = False
try:
    iskeyword
    result = False
except NameError:
    iskeyword_missing = True

keyword.__all__ = ["iskeyword", "softkwlist"]
from keyword import *

result = result and iskeyword("for")
result = result and "type" in softkwlist

issoftkeyword_missing = False
try:
    issoftkeyword
    result = False
except NameError:
    issoftkeyword_missing = True

result = result and iskeyword_missing and issoftkeyword_missing

result
