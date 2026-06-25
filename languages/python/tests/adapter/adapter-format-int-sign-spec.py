result = format(10, "+d") == "+10"
result = result and format(-10, "+d") == "-10"
result = result and format(0, "+d") == "+0"
result = result and format(True, "+d") == "+1"
result = result and format(10, " d") == " 10"
result = result and format(-10, " d") == "-10"
result = result and format(False, " d") == " 0"
result = result and format(10, "-d") == "10"
result = result and format(-10, "-d") == "-10"

assert result
result
