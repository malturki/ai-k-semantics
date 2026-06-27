os_error = False
try:
    raise FileNotFoundError
except OSError:
    os_error = True

connection = False
try:
    raise ConnectionResetError
except ConnectionError:
    connection = True

module = False
try:
    raise ModuleNotFoundError
except ImportError:
    module = True

runtime = False
try:
    raise RecursionError
except RuntimeError:
    runtime = True

unicode_value = False
try:
    raise UnicodeError
except ValueError:
    unicode_value = True

warning = False
try:
    raise SyntaxWarning
except Warning:
    warning = True

keyboard = 0
try:
    raise KeyboardInterrupt
except Exception:
    keyboard = 10
except BaseException:
    keyboard = 1

system_exit = 0
try:
    raise SystemExit
except Exception:
    system_exit = 10
except BaseException:
    system_exit = 1

alias = False
try:
    raise IOError
except OSError:
    alias = True

incomplete = False
try:
    raise _IncompleteInputError
except SyntaxError:
    incomplete = True

result = (
    os_error
    and connection
    and module
    and runtime
    and unicode_value
    and warning
    and keyboard == 1
    and system_exit == 1
    and alias
    and incomplete
)
assert result
result
