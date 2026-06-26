latin1 = "é"
latin1_quote = "é'"
bmp = "Ā"
greek = "Ω"
cjk = "中"
face = "😀"
control = "\x80"
latin1_max = "\xff"
plane1 = "\U00010000"

assert repr(latin1) == "'é'"
assert ascii(latin1) == "'\\xe9'"
assert ascii(latin1_quote) == "\"\\xe9'\""
assert ascii(control) == "'\\x80'"
assert ascii(latin1_max) == "'\\xff'"
assert ascii(bmp) == "'\\u0100'"
assert ascii(greek) == "'\\u03a9'"
assert ascii(cjk) == "'\\u4e2d'"
assert ascii(face) == "'\\U0001f600'"
assert ascii(plane1) == "'\\U00010000'"

mixed = "AéĀ😀\n\x7f"
assert ascii(mixed) == "'A\\xe9\\u0100\\U0001f600\\n\\x7f'"

nested = [latin1, {"face": face}, (bmp,)]
assert ascii(nested) == "['\\xe9', {'face': '\\U0001f600'}, ('\\u0100',)]"
assert ascii(slice(latin1, None, (bmp,))) == "slice('\\xe9', None, ('\\u0100',))"

assert f"{latin1!a}:{nested!a}" == "'\\xe9':['\\xe9', {'face': '\\U0001f600'}, ('\\u0100',)]"
assert f"{latin1!a:>8}" == "  '\\xe9'"
assert f"{face!a:^16}" == "  '\\U0001f600'  "

result = ascii([latin1, bmp, face])
result == "['\\xe9', '\\u0100', '\\U0001f600']"
