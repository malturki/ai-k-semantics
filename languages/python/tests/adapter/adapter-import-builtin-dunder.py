import importlib
import keyword
import math


saved_import = __import__
shadow_before_restore = False
__import__ = 17
shadow_before_restore = __import__ == 17
__import__ = saved_import

math.dynamic_import_value = 314

dotted_missing_module = False
try:
    __import__("math.foo")
except ModuleNotFoundError:
    dotted_missing_module = True

missing_module = False
try:
    __import__("not_a_real_module_for_k_semantics")
except ModuleNotFoundError:
    missing_module = True

relative_name = False
try:
    __import__(".keyword")
except ValueError:
    relative_name = True

empty_name = False
try:
    __import__("")
except ValueError:
    empty_name = True

non_string_name = False
try:
    __import__(1)
except TypeError:
    non_string_name = True

wrong_arity = False
try:
    __import__()
except TypeError:
    wrong_arity = True

negative_level = False
try:
    __import__("math", None, None, [], -1)
except ValueError:
    negative_level = True

non_int_level = False
try:
    __import__("math", None, None, [], "1")
except TypeError:
    non_int_level = True

duplicate_name = False
try:
    __import__("math", name="keyword")
except TypeError:
    duplicate_name = True

bad_keyword = False
try:
    __import__("math", bogus=1)
except TypeError:
    bad_keyword = True

importlib_dotted_missing_module = False
try:
    importlib.__import__("math.foo")
except ModuleNotFoundError:
    importlib_dotted_missing_module = True

result = (
    callable(__import__)
    and callable(importlib.__import__)
    and saved_import is __import__
    and shadow_before_restore
    and __import__("math") is math
    and __import__("keyword", None, None, ["iskeyword"]) is keyword
    and __import__("importlib") is importlib
    and __import__("math", None, None, ["pi"], 0) is math
    and __import__(name="keyword") is keyword
    and __import__("math", fromlist=["pi"]) is math
    and __import__("math", level=0) is math
    and importlib.__import__("math") is math
    and importlib.__import__("keyword", None, None, ["kwlist"]) is keyword
    and __import__("math").dynamic_import_value == 314
    and importlib.__import__("math").dynamic_import_value == 314
    and dotted_missing_module
    and missing_module
    and relative_name
    and empty_name
    and non_string_name
    and wrong_arity
    and negative_level
    and non_int_level
    and duplicate_name
    and bad_keyword
    and importlib_dotted_missing_module
)

result
