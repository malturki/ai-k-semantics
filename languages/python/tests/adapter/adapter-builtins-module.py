import builtins
import builtins as b
import importlib
import math
from builtins import __debug__ as builtin_debug
from builtins import __import__ as builtin_import
from builtins import Ellipsis as builtin_ellipsis


missing_from = False
try:
    from builtins import not_a_real_builtin_for_k
except ImportError:
    missing_from = True

star_original_ellipsis = Ellipsis
Ellipsis = 17
shadowed_import = __import__
__import__ = 5
from builtins import *
star_rebound_ellipsis = Ellipsis is star_original_ellipsis
star_excludes_dunder_import = __import__ == 5
__import__ = shadowed_import

builtins.dynamic = 271
from builtins import dynamic as imported_dynamic

again = __import__("builtins")
via_importlib = importlib.import_module("builtins")
via_builtin_import = builtins.__import__("builtins")

result = (
    builtins.__name__ == "builtins"
    and b is builtins
    and builtin_import is __import__
    and builtins.__import__ is __import__
    and getattr(builtins, "__import__") is __import__
    and builtins.__import__("math") is math
    and __import__("builtins") is builtins
    and importlib.import_module("builtins") is builtins
    and builtins.Ellipsis is Ellipsis
    and builtin_ellipsis is Ellipsis
    and getattr(builtins, "Ellipsis") is Ellipsis
    and builtins.__debug__ is __debug__
    and builtin_debug is __debug__
    and getattr(builtins, "__debug__") is __debug__
    and getattr(builtins, "None") is None
    and getattr(builtins, "True") is True
    and getattr(builtins, "False") is False
    and not hasattr(builtins, "__all__")
    and star_rebound_ellipsis
    and star_excludes_dunder_import
    and missing_from
    and imported_dynamic == 271
    and again is builtins
    and via_importlib is builtins
    and via_builtin_import is builtins
    and again.dynamic == 271
    and via_importlib.dynamic == 271
    and via_builtin_import.dynamic == 271
)

result
