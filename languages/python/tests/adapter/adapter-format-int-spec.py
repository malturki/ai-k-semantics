result = format(10, "b") == "1010"
result = result and format(-10, "b") == "-1010"
result = result and format(True, "b") == "1"
result = result and format(False, "d") == "0"
result = result and format(10, "o") == "12"
result = result and format(10, "d") == "10"
result = result and format(255, "x") == "ff"
result = result and format(255, "X") == "FF"
result = result and format(65, "c") == "A"
result = result and format(True, "c") == "\x01"

negative_char_overflow = False
try:
    format(-1, "c")
except OverflowError:
    negative_char_overflow = True

high_char_overflow = False
try:
    format(1114112, "c")
except OverflowError:
    high_char_overflow = True

result = result and negative_char_overflow and high_char_overflow

assert result
result
