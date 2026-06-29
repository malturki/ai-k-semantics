error_data = b"abc"

errors_ok = True

try:
    error_data.find(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.find(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.find(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.find("a")
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(300)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(-1)
except ValueError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind(1.0)
except TypeError:
    pass
else:
    errors_ok = False

try:
    error_data.rfind("a")
except TypeError:
    pass
else:
    errors_ok = False

result = errors_ok and error_data == b"abc"
assert result
result
