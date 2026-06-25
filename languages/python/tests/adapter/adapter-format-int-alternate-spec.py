result = format(10, "#b") == "0b1010"
result = result and format(-10, "#b") == "-0b1010"
result = result and format(True, "#b") == "0b1"
result = result and format(0, "#b") == "0b0"
result = result and format(10, "#o") == "0o12"
result = result and format(-10, "#o") == "-0o12"
result = result and format(255, "#x") == "0xff"
result = result and format(-255, "#x") == "-0xff"
result = result and format(255, "#X") == "0XFF"
result = result and format(-255, "#X") == "-0XFF"
result = result and format(10, "#d") == "10"
result = result and format(-10, "#d") == "-10"

assert result
result
