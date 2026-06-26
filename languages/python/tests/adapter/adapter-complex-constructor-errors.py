complex_empty_string = False
try:
    complex("")
except ValueError:
    complex_empty_string = True

complex_blank_string = False
try:
    complex("   ")
except ValueError:
    complex_blank_string = True

complex_bad_name = False
try:
    complex("abc")
except ValueError:
    complex_bad_name = True

complex_missing_imaginary_suffix = False
try:
    complex("1+2")
except ValueError:
    complex_missing_imaginary_suffix = True

complex_bad_underscore = False
try:
    complex("1__0")
except ValueError:
    complex_bad_underscore = True

complex_unbalanced_open = False
try:
    complex("(1+2j")
except ValueError:
    complex_unbalanced_open = True

complex_unbalanced_close = False
try:
    complex("1+2j)")
except ValueError:
    complex_unbalanced_close = True

complex_internal_space = False
try:
    complex("1 + 2j")
except ValueError:
    complex_internal_space = True

complex_bytes_type = False
try:
    complex(b"1")
except TypeError:
    complex_bytes_type = True

complex_bytearray_type = False
try:
    complex(bytearray(b"1"))
except TypeError:
    complex_bytearray_type = True

complex_list_type = False
try:
    complex([])
except TypeError:
    complex_list_type = True

complex_tuple_type = False
try:
    complex(())
except TypeError:
    complex_tuple_type = True

complex_dict_type = False
try:
    complex({})
except TypeError:
    complex_dict_type = True

complex_set_type = False
try:
    complex(set())
except TypeError:
    complex_set_type = True

complex_range_type = False
try:
    complex(range(2))
except TypeError:
    complex_range_type = True

complex_none_type = False
try:
    complex(None)
except TypeError:
    complex_none_type = True

complex_ellipsis_type = False
try:
    complex(Ellipsis)
except TypeError:
    complex_ellipsis_type = True

complex_string_two_arg_type = False
try:
    complex("1", 2)
except TypeError:
    complex_string_two_arg_type = True

complex_bad_real_type = False
try:
    complex([], 1)
except TypeError:
    complex_bad_real_type = True

complex_bad_imag_type = False
try:
    complex(1, [])
except TypeError:
    complex_bad_imag_type = True

result = (
    complex_empty_string
    and complex_blank_string
    and complex_bad_name
    and complex_missing_imaginary_suffix
    and complex_bad_underscore
    and complex_unbalanced_open
    and complex_unbalanced_close
    and complex_internal_space
    and complex_bytes_type
    and complex_bytearray_type
    and complex_list_type
    and complex_tuple_type
    and complex_dict_type
    and complex_set_type
    and complex_range_type
    and complex_none_type
    and complex_ellipsis_type
    and complex_string_two_arg_type
    and complex_bad_real_type
    and complex_bad_imag_type
)
assert result
result
