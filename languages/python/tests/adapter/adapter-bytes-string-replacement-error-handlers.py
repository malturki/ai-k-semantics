text = "A\xe9\u03a9\U0001f600"
latin_text = "A\xe9\u0100\U0001f600"

result = bytes(text, "ascii", "backslashreplace") == b"A\\xe9\\u03a9\\U0001f600"
result = result and bytes(latin_text, "ascii", "backslashreplace") == b"A\\xe9\\u0100\\U0001f600"
result = result and bytes(text, "latin-1", "backslashreplace") == b"A\xe9\\u03a9\\U0001f600"
result = result and bytes(latin_text, "latin-1", "backslashreplace") == b"A\xe9\\u0100\\U0001f600"

result = result and bytes(text, "ascii", "xmlcharrefreplace") == b"A&#233;&#937;&#128512;"
result = result and bytes(latin_text, "ascii", "xmlcharrefreplace") == b"A&#233;&#256;&#128512;"
result = result and bytes(text, "latin-1", "xmlcharrefreplace") == b"A\xe9&#937;&#128512;"
result = result and bytes(latin_text, "latin-1", "xmlcharrefreplace") == b"A\xe9&#256;&#128512;"

result = result and bytes("abc", "ascii", "backslashreplace") == b"abc"
result = result and bytes("abc", "latin-1", "xmlcharrefreplace") == b"abc"

assert result
result
