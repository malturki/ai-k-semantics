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

del kwlist
keyword.__all__ = ("kwlist",)
from keyword import *
result = result and "False" in kwlist

del kwlist
partial_attribute_error = False
try:
    keyword.__all__ = ["kwlist", "never_there"]
    from keyword import *
    result = False
except AttributeError:
    partial_attribute_error = True

result = result and partial_attribute_error
result = result and "False" in kwlist

del kwlist
partial_type_error = False
try:
    keyword.__all__ = ["kwlist", 1]
    from keyword import *
    result = False
except TypeError:
    partial_type_error = True

result = result and partial_type_error
result = result and "False" in kwlist

del kwlist
setattr(keyword, "dynamic", 77)
keyword.__all__ = ["dynamic"]
from keyword import *
result = result and dynamic == 77

del dynamic
keyword.__all__ = ""
from keyword import *

empty_string_all_missing = False
try:
    kwlist
    result = False
except NameError:
    empty_string_all_missing = True

result = result and empty_string_all_missing

result
