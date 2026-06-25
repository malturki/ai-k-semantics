result = format("abcdef", ".3") == "abc"
result = result and format("abcdef", ".3s") == "abc"
result = result and format("abcdef", "8.3") == "abc     "
result = result and format("abcdef", ">8.3s") == "     abc"
result = result and format("abcdef", "<8.3s") == "abc     "
result = result and format("abcdef", "^8.3s") == "  abc   "
result = result and format("abcdef", "*^8.3s") == "**abc***"
result = result and format("abcdef", "08.3s") == "abc00000"
result = result and format("abcdef", ".0s") == ""
result = result and format("abc", ".5s") == "abc"

dot_error = False
try:
    format("abcdef", ".")
except ValueError:
    dot_error = True

dot_type_error = False
try:
    format("abcdef", ".s")
except ValueError:
    dot_type_error = True

width_dot_type_error = False
try:
    format("abcdef", "5.s")
except ValueError:
    width_dot_type_error = True

result = result and dot_error and dot_type_error and width_dot_type_error

assert result
result
