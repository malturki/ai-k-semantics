result = min("cba") == "a"
result = result and max("abc") == "c"
result = result and min("bbab") == "a"
result = result and max("bbcb") == "c"

result = result and min("bca", default="z") == "a"
result = result and max("bca", default="") == "c"
result = result and min("", default="z") == "z"
result = result and max("", default="z") == "z"

result = result and min("cba", key=None) == "a"
result = result and max("abc", key=None, default="") == "c"
result = result and min("cba", default="z", key=None) == "a"

min_empty_string_error = False
try:
    min("")
except ValueError:
    min_empty_string_error = True

max_empty_string_error = False
try:
    max("")
except ValueError:
    max_empty_string_error = True

result = result and min_empty_string_error and max_empty_string_error
assert result
result
