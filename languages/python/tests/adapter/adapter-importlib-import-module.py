import importlib
import keyword
import math
from importlib import import_module as im


missing_module = False
try:
    im("not_a_real_module_for_k_semantics")
except ModuleNotFoundError:
    missing_module = True

relative_without_package = False
try:
    im(".keyword")
except TypeError:
    relative_without_package = True

non_string_name = False
try:
    im(1)
except AttributeError:
    non_string_name = True

non_string_name_with_package = False
try:
    im(1, None)
except AttributeError:
    non_string_name_with_package = True

empty_name = False
try:
    im("")
except ValueError:
    empty_name = True

wrong_arity = False
try:
    im()
except TypeError:
    wrong_arity = True

result = (
    importlib.__name__ == "importlib"
    and callable(importlib.import_module)
    and importlib.import_module is im
    and importlib.import_module == im
    and im("math") is math
    and im("keyword") is keyword
    and im("importlib") is importlib
    and im("math", None) is math
    and missing_module
    and relative_without_package
    and non_string_name
    and non_string_name_with_package
    and empty_name
    and wrong_arity
)

result
