single_quote = "don't"
double_quote = 'quote"'
both_quotes = 'both\'"'
backslash = "\\"
named_controls = "\t\n\r"

assert repr(single_quote) == "\"don't\""
assert repr(double_quote) == "'quote\"'"
assert repr(both_quotes) == "'both\\'\"'"
assert repr(backslash) == "'\\\\'"
assert repr(named_controls) == "'\\t\\n\\r'"
assert ascii(named_controls) == "'\\t\\n\\r'"

values = [single_quote, named_controls, backslash]
assert repr(values) == "[\"don't\", '\\t\\n\\r', '\\\\']"

result = f"{single_quote!r}:{named_controls!a}:{values!r}"
result == "\"don't\":'\\t\\n\\r':[\"don't\", '\\t\\n\\r', '\\\\']"
