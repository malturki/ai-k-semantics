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

relative_multi = False
try:
    from . import math, keyword as local_keyword
except ImportError:
    relative_multi = True

relative_module_multi = False
try:
    from .keyword import kwlist as local_kwlist, softkwlist
except ImportError:
    relative_module_multi = True

result = (
    relative_bare
    and relative_alias
    and relative_module_attr
    and relative_parent
    and relative_multi
    and relative_module_multi
)
assert result
result
