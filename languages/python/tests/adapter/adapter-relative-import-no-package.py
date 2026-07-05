relative_bare = False
try:
    from . import math
except ImportError:
    relative_bare = True

relative_alias = False
try:
    from . import keyword as local_keyword
except ImportError:
    relative_alias = True

relative_module_attr = False
try:
    from .keyword import kwlist as local_kwlist
except ImportError:
    relative_module_attr = True

relative_parent = False
try:
    from .. import math
except ImportError:
    relative_parent = True

result = relative_bare and relative_alias and relative_module_attr and relative_parent
assert result
result
