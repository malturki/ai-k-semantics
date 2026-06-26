euro = chr(8364)
omega = chr(937)
latin1 = chr(255)
plane1 = chr(0x10000)
max_char = chr(0x10ffff)

result = euro == "\u20ac"
result = result and omega == "\u03a9"
result = result and latin1 == "\xff"
result = result and plane1 == "\U00010000"

result = result and ord(euro) == 8364
result = result and ord(omega) == 937
result = result and ord(latin1) == 255
result = result and ord(plane1) == 0x10000
result = result and ord(max_char) == 0x10ffff

result = result and ord("\u20ac") == 8364
result = result and ord("\U00010000") == 0x10000

result = result and ascii(euro) == "'\\u20ac'"
result = result and ascii(plane1) == "'\\U00010000'"
result = result and ascii(max_char) == "'\\U0010ffff'"
result = result and f"{euro!a}:{plane1!a}" == "'\\u20ac':'\\U00010000'"

result = result and format(8364, "c") == euro
result = result and format(0x10000, "c") == plane1

assert result
result
