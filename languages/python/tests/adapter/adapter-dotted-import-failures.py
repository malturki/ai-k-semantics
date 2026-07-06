result = True

dotted_import = False
try:
    import math.foo
    result = False
except ModuleNotFoundError:
    dotted_import = True

math_missing = False
try:
    math
    result = False
except NameError:
    math_missing = True

dotted_import_as = False
try:
    import math.foo as math_foo
    result = False
except ModuleNotFoundError:
    dotted_import_as = True

alias_missing = False
try:
    math_foo
    result = False
except NameError:
    alias_missing = True

dotted_from_import = False
try:
    from math.foo import bar
    result = False
except ModuleNotFoundError:
    dotted_from_import = True

dotted_from_import_as = False
try:
    from math.foo import bar as local_bar
    result = False
except ModuleNotFoundError:
    dotted_from_import_as = True

from_alias_missing = False
try:
    local_bar
    result = False
except NameError:
    from_alias_missing = True

dotted_from_import_star = False
try:
    from math.foo import *
    result = False
except ModuleNotFoundError:
    dotted_from_import_star = True

result = (
    result
    and dotted_import
    and math_missing
    and dotted_import_as
    and alias_missing
    and dotted_from_import
    and dotted_from_import_as
    and from_alias_missing
    and dotted_from_import_star
)

result
