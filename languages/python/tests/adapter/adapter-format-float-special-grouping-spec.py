pos = float("inf")
neg = float("-inf")
nan = float("nan")

result = format(pos, ",f") == "inf"
result = result and format(neg, "_f") == "-inf"
result = result and format(pos, "8,f") == "     inf"
result = result and format(neg, "8_f") == "    -inf"
result = result and format(nan, ",g") == "nan"
result = result and format(pos, "_G") == "INF"
result = result and format(neg, ",%") == "-inf%"
result = result and format(nan, "_%") == "nan%"

comma_n_error = False
try:
    format(pos, ",n")
except ValueError:
    comma_n_error = True

underscore_n_error = False
try:
    format(neg, "8_n")
except ValueError:
    underscore_n_error = True

z_comma_n_error = False
try:
    format(nan, "z,n")
except ValueError:
    z_comma_n_error = True

result = result and comma_n_error and underscore_n_error and z_comma_n_error

assert result
result
