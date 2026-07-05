floating = False
try:
    raise FloatingPointError
except ArithmeticError:
    floating = True

overflow = False
try:
    raise OverflowError
except ArithmeticError:
    overflow = True

not_implemented = False
try:
    raise NotImplementedError
except RuntimeError:
    not_implemented = True

finalization = False
try:
    raise PythonFinalizationError
except RuntimeError:
    finalization = True

stop_iteration = False
try:
    raise StopIteration
except Exception:
    stop_iteration = True

stop_async_iteration = False
try:
    raise StopAsyncIteration
except Exception:
    stop_async_iteration = True

generator_exit = 0
try:
    raise GeneratorExit
except Exception:
    generator_exit = 10
except BaseException:
    generator_exit = 1

system_exit = 0
try:
    raise SystemExit
except Exception:
    system_exit = 10
except BaseException:
    system_exit = 1

tab_error = False
try:
    raise TabError
except IndentationError:
    tab_error = True

indentation_error = False
try:
    raise IndentationError
except SyntaxError:
    indentation_error = True

buffer_error = False
try:
    raise BufferError
except Exception:
    buffer_error = True

eof_error = False
try:
    raise EOFError
except Exception:
    eof_error = True

warning_count = 0
try:
    raise DeprecationWarning
except Warning:
    warning_count = warning_count + 1

try:
    raise EncodingWarning
except Warning:
    warning_count = warning_count + 1

try:
    raise ResourceWarning
except Warning:
    warning_count = warning_count + 1

try:
    raise UnicodeWarning
except Warning:
    warning_count = warning_count + 1

result = (
    floating
    and overflow
    and not_implemented
    and finalization
    and stop_iteration
    and stop_async_iteration
    and generator_exit == 1
    and system_exit == 1
    and tab_error
    and indentation_error
    and buffer_error
    and eof_error
    and warning_count == 4
)
assert result
result
