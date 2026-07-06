def mark_type_error(thunk):
    try:
        thunk()
    except TypeError:
        return True
    return False


def class_metadata(value, expected_name):
    cls = type(value)
    return (
        value.__class__ is cls
        and getattr(value, "__class__") is cls
        and hasattr(value, "__class__")
        and isinstance(value, cls)
        and cls.__name__ == expected_name
        and cls.__qualname__ == expected_name
        and cls.__module__ == "builtins"
        and str(cls) == "<class '" + expected_name + "'>"
        and repr(cls) == "<class '" + expected_name + "'>"
        and ascii(cls) == "<class '" + expected_name + "'>"
    )


bool_value = True
int_value = 7
float_value = 1.5
complex_value = 1 + 2j
str_value = "x"
bytes_value = b"x"
bytearray_value = bytearray(b"x")
memoryview_value = memoryview(b"x")
list_value = [1]
tuple_value = (1,)
dict_value = {"x": 1}
set_value = {1}
frozenset_value = frozenset({1})
range_value = range(2)
slice_value = slice(1)

bool_type = type(bool_value)
int_type = type(int_value)
float_type = type(float_value)
complex_type = type(complex_value)
str_type = type(str_value)
bytes_type = type(bytes_value)
bytearray_type = type(bytearray_value)
list_type = type(list_value)
tuple_type = type(tuple_value)
dict_type = type(dict_value)
set_type = type(set_value)
frozenset_type = type(frozenset_value)
range_type = type(range_value)
slice_type = type(slice_value)
memoryview_type = type(memoryview_value)


def range_without_arguments():
    range_type()


def slice_without_arguments():
    slice_type()


def memoryview_without_arguments():
    memoryview_type()


bool_metadata = class_metadata(bool_value, "bool")
int_metadata = class_metadata(int_value, "int")
float_metadata = class_metadata(float_value, "float")
complex_metadata = class_metadata(complex_value, "complex")
str_metadata = class_metadata(str_value, "str")
bytes_metadata = class_metadata(bytes_value, "bytes")
bytearray_metadata = class_metadata(bytearray_value, "bytearray")
memoryview_metadata = class_metadata(memoryview_value, "memoryview")
list_metadata = class_metadata(list_value, "list")
tuple_metadata = class_metadata(tuple_value, "tuple")
dict_metadata = class_metadata(dict_value, "dict")
set_metadata = class_metadata(set_value, "set")
frozenset_metadata = class_metadata(frozenset_value, "frozenset")
range_metadata = class_metadata(range_value, "range")
slice_metadata = class_metadata(slice_value, "slice")

bool_constructor = bool_type() is False
int_constructor = int_type() == 0
float_constructor = float_type() == 0.0
complex_constructor = complex_type() == 0j
str_constructor = str_type() == ""
bytes_constructor = bytes_type() == b""
bytearray_constructor = bytearray_type() == bytearray()
list_constructor = list_type() == []
tuple_constructor = tuple_type() == ()
dict_constructor = dict_type() == {}
set_constructor = set_type() == set()
frozenset_constructor = frozenset_type() == frozenset()
bool_int_subclass = issubclass(bool_type, int_type)
int_bool_not_subclass = not issubclass(int_type, bool_type)
range_noarg_error = mark_type_error(range_without_arguments)
slice_noarg_error = mark_type_error(slice_without_arguments)
memoryview_noarg_error = mark_type_error(memoryview_without_arguments)

result = (
    bool_metadata
    and int_metadata
    and float_metadata
    and complex_metadata
    and str_metadata
    and bytes_metadata
    and bytearray_metadata
    and memoryview_metadata
    and list_metadata
    and tuple_metadata
    and dict_metadata
    and set_metadata
    and frozenset_metadata
    and range_metadata
    and slice_metadata
    and bool_constructor
    and int_constructor
    and float_constructor
    and complex_constructor
    and str_constructor
    and bytes_constructor
    and bytearray_constructor
    and list_constructor
    and tuple_constructor
    and dict_constructor
    and set_constructor
    and frozenset_constructor
    and bool_int_subclass
    and int_bool_not_subclass
    and range_noarg_error
    and slice_noarg_error
    and memoryview_noarg_error
)

result
