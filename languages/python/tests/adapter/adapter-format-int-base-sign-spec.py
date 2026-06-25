result = format(10, "+b") == "+1010"
result = result and format(-10, "+b") == "-1010"
result = result and format(False, "+b") == "+0"
result = result and format(10, " b") == " 1010"
result = result and format(-10, " b") == "-1010"
result = result and format(10, "-b") == "1010"
result = result and format(10, "+o") == "+12"
result = result and format(-10, " o") == "-12"
result = result and format(255, "+x") == "+ff"
result = result and format(-255, " x") == "-ff"
result = result and format(255, "+X") == "+FF"
result = result and format(255, " X") == " FF"
result = result and format(-255, "-X") == "-FF"

result = result and format(10, "+#b") == "+0b1010"
result = result and format(-10, "+#b") == "-0b1010"
result = result and format(False, " #b") == " 0b0"
result = result and format(10, "-#b") == "0b1010"
result = result and format(10, "+#d") == "+10"
result = result and format(-10, " #d") == "-10"
result = result and format(10, "-#d") == "10"
result = result and format(10, "+#o") == "+0o12"
result = result and format(-10, " #o") == "-0o12"
result = result and format(255, "+#x") == "+0xff"
result = result and format(-255, " #x") == "-0xff"
result = result and format(255, "+#X") == "+0XFF"
result = result and format(255, " #X") == " 0XFF"
result = result and format(-255, "-#X") == "-0XFF"

plus_char_error = False
try:
    format(65, "+c")
except ValueError:
    plus_char_error = True

space_char_error = False
try:
    format(65, " c")
except ValueError:
    space_char_error = True

minus_char_error = False
try:
    format(65, "-c")
except ValueError:
    minus_char_error = True

result = result and plus_char_error and space_char_error and minus_char_error

assert result
result
