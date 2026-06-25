result = format("abc", "s") == "abc"
result = result and format("abc", "5") == "abc  "
result = result and format("abc", "<5") == "abc  "
result = result and format("abc", ">5") == "  abc"
result = result and format("abc", "^5") == " abc "
result = result and format("abc", "*<5") == "abc**"
result = result and format("abc", "*>5") == "**abc"
result = result and format("abc", "*^6") == "*abc**"
result = result and format("abc", "05") == "abc00"
result = result and format("abc", "0>5s") == "00abc"

result = result and format(10, "5") == "   10"
result = result and format(10, "5d") == "   10"
result = result and format(10, "<5d") == "10   "
result = result and format(10, ">5d") == "   10"
result = result and format(10, "^5d") == " 10  "
result = result and format(10, "*>5d") == "***10"
result = result and format(-10, "5d") == "  -10"
result = result and format(-10, "=5d") == "-  10"
result = result and format(10, "05d") == "00010"
result = result and format(-10, "05d") == "-0010"
result = result and format(10, "+05d") == "+0010"
result = result and format(-10, "+05d") == "-0010"
result = result and format(False, "05") == "00000"
result = result and format(True, "+05") == "+0001"

result = result and format(10, "#") == "10"
result = result and format(10, "#06x") == "0x000a"
result = result and format(-10, "#06x") == "-0x00a"
result = result and format(10, "*>#6x") == "***0xa"
result = result and format(10, "*<#6x") == "0xa***"
result = result and format(10, "*^#6x") == "*0xa**"
result = result and format(10, "*=#6x") == "0x***a"
result = result and format(False, "#06x") == "0x0000"

result = result and format(65, "5c") == "    A"
result = result and format(65, "*<5c") == "A****"
result = result and format(65, "05c") == "0000A"

sign_char_error = False
try:
    format(65, "+#05c")
except ValueError:
    sign_char_error = True

alternate_char_error = False
try:
    format(65, "#5c")
except ValueError:
    alternate_char_error = True

result = result and sign_char_error and alternate_char_error

assert result
result
