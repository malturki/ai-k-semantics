named = "\N{LATIN CAPITAL LETTER A}\N{LATIN CAPITAL LETTER B}"
hex_oct = "\x43\104"
raw = r"\n\t\x45"
ignored_newline = "left\
right"
triple = """top
bottom"""
adjacent = "py" "thon" r"\n" "\x21"

strings_ok = named == "AB"
strings_ok = strings_ok and hex_oct == "CD"
strings_ok = strings_ok and raw == "\\n\\t\\x45"
strings_ok = strings_ok and ignored_newline == "leftright"
strings_ok = strings_ok and triple == "top\nbottom"
strings_ok = strings_ok and adjacent == "python\\n!"
strings_ok = strings_ok and ord("\n") == 10 and ord("\t") == 9

escaped = b"\x00\001\x41\177\200\377"
raw_bytes = rb"\n\x41"
adjacent_bytes = b"A" b"\x42" rb"\x43"

bytes_ok = len(escaped) == 6
bytes_ok = bytes_ok and escaped[0] == 0 and escaped[1] == 1
bytes_ok = bytes_ok and escaped[2] == 65 and escaped[3] == 127
bytes_ok = bytes_ok and escaped[4] == 128 and escaped[5] == 255
bytes_ok = bytes_ok and raw_bytes == b"\\n\\x41"
bytes_ok = bytes_ok and adjacent_bytes == b"AB\\x43"
bytes_ok = bytes_ok and repr(escaped) == "b'\\x00\\x01A\\x7f\\x80\\xff'"

result = strings_ok and bytes_ok
assert result
result
