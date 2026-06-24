assert repr(b"") == "b''"
assert str(b"abc") == "b'abc'"
assert ascii(b'has "quote"') == "b'has \"quote\"'"
assert repr(b"don't") == "b\"don't\""
assert repr(b"'\"") == "b'\\'\"'"
assert repr(b"\\") == "b'\\\\'"
assert repr(b"\t\n\r") == "b'\\t\\n\\r'"

all_bytes = b"\x00\x07\x08\t\n\x0b\x0c\r\x1b\x1f !\"#'\\~\x7f\x80\xff"
expected = "b'\\x00\\x07\\x08\\t\\n\\x0b\\x0c\\r\\x1b\\x1f !\"#\\'\\\\~\\x7f\\x80\\xff'"
assert repr(all_bytes) == expected

result = repr([b"AZ", b"\x00"])
assert result == "[b'AZ', b'\\x00']"

nl = b"\n"
tab = b"\t"
assert f"{b'AZ'}:{nl!r}:{tab!a}" == "b'AZ':b'\\n':b'\\t'"

result == "[b'AZ', b'\\x00']"
