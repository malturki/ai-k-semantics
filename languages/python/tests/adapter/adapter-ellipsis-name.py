literal = ...
builtin = Ellipsis

result = builtin is literal
result = result and Ellipsis is ...
result = result and bool(Ellipsis)

Ellipsis = 7
result = result and Ellipsis == 7
result = result and builtin is literal

del Ellipsis
result = result and Ellipsis is literal

Ellipsis = ...
result = result and Ellipsis is builtin

assert result
result
