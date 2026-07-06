import builtins
from builtins import int as imported_int
from builtins import list as imported_list
from builtins import memoryview as imported_memoryview
from builtins import range as imported_range


def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


def mark_name_error(thunk):
    try:
        thunk()
    except NameError:
        return True
    return False


def none_type_name():
    NoneType


def ellipsis_type_name():
    EllipsisType


bool_alias = bool
int_alias = int
float_alias = float
complex_alias = complex
str_alias = str
bytes_alias = bytes
bytearray_alias = bytearray
list_alias = list
tuple_alias = tuple
dict_alias = dict
set_alias = set
frozenset_alias = frozenset
range_alias = range
slice_alias = slice
memoryview_alias = memoryview


def range_without_arguments():
    range_alias()


def slice_without_arguments():
    slice_alias()


def memoryview_without_arguments():
    memoryview_alias()


bare_identities = (
    bool is type(True)
    and int is type(1)
    and float is type(1.0)
    and complex is type(1j)
    and str is type("")
    and bytes is type(b"")
    and bytearray is type(bytearray())
    and memoryview is type(memoryview(b""))
    and list is type([])
    and tuple is type(())
    and dict is type({})
    and set is type(set())
    and frozenset is type(frozenset())
    and range is type(range(0))
    and slice is type(slice(1))
)

module_identities = (
    builtins.bool is bool
    and builtins.int is int
    and builtins.float is float
    and builtins.complex is complex
    and builtins.str is str
    and builtins.bytes is bytes
    and builtins.bytearray is bytearray
    and builtins.memoryview is memoryview
    and builtins.list is list
    and builtins.tuple is tuple
    and builtins.dict is dict
    and builtins.set is set
    and builtins.frozenset is frozenset
    and builtins.range is range
    and builtins.slice is slice
    and getattr(builtins, "int") is int
    and getattr(builtins, "list") is list
    and getattr(builtins, "memoryview") is memoryview
    and hasattr(builtins, "range")
)

from_import_identities = (
    imported_int is int
    and imported_list is list
    and imported_memoryview is memoryview
    and imported_range is range
)

dynamic_classinfo = (
    isinstance(1, int)
    and isinstance([], list)
    and isinstance(memoryview(b"x"), memoryview)
    and issubclass(bool, int)
    and not issubclass(int, bool)
)

alias_constructors = (
    bool_alias() is False
    and int_alias() == 0
    and float_alias() == 0.0
    and complex_alias() == 0j
    and str_alias() == ""
    and bytes_alias() == b""
    and bytearray_alias() == bytearray()
    and list_alias() == []
    and tuple_alias() == ()
    and dict_alias() == {}
    and set_alias() == set()
    and frozenset_alias() == frozenset()
    and mark_type_error(range_without_arguments)
    and mark_type_error(slice_without_arguments)
    and mark_type_error(memoryview_without_arguments)
)

bool = "shadowed"
shadow_fallback = bool == "shadowed" and bool_alias is builtins.bool

int = 271
list = "list-shadow"
__import__ = "dunder-shadow"
from builtins import *
star_without_all = (
    int is builtins.int
    and list is builtins.list
    and bool is builtins.bool
    and __import__ == "dunder-shadow"
)

int = 1
list = 2
memoryview = 3
float = 4
builtins.__all__ = ["int", "list", "memoryview"]
from builtins import *
star_with_all = (
    int is builtins.int
    and list is builtins.list
    and memoryview is builtins.memoryview
    and float == 4
)

singleton_type_names_not_bare_builtins = (
    mark_name_error(none_type_name)
    and mark_name_error(ellipsis_type_name)
)

result = (
    bare_identities
    and module_identities
    and from_import_identities
    and dynamic_classinfo
    and alias_constructors
    and shadow_fallback
    and star_without_all
    and star_with_all
    and singleton_type_names_not_bare_builtins
)

result
