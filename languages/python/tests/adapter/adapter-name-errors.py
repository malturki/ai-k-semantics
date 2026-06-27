module_name_error = False
try:
    missing_name
except NameError:
    module_name_error = True

gone = 1
del gone
deleted_name_error = False
try:
    gone
except NameError:
    deleted_name_error = True


def read_missing():
    return missing_inside_function


function_name_error = False
try:
    read_missing()
except NameError:
    function_name_error = True

result = module_name_error and deleted_name_error and function_name_error
assert result
result
