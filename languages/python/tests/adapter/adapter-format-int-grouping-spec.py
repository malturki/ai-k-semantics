result = format(1234567, ",d") == "1,234,567"
result = result and format(1234567, ",") == "1,234,567"
result = result and format(-1234567, ",d") == "-1,234,567"
result = result and format(1234567, "12,d") == "   1,234,567"
result = result and format(1234567, "012,d") == "0,001,234,567"
result = result and format(-1234567, "012,d") == "-001,234,567"
result = result and format(1234567, "_d") == "1_234_567"
result = result and format(1234567, "_") == "1_234_567"
result = result and format(-1234567, "_d") == "-1_234_567"
result = result and format(1234567, "12_d") == "   1_234_567"

result = result and format(0x12345678, "_x") == "1234_5678"
result = result and format(0x12345678, "#_x") == "0x1234_5678"
result = result and format(0x12345678, "#12_x") == " 0x1234_5678"
result = result and format(0x12345678, "_X") == "1234_5678"
result = result and format(0o12345670, "_o") == "1234_5670"
result = result and format(0b1010101111001101, "_b") == "1010_1011_1100_1101"
result = result and format(1234567, "#012_x") == "0x0_0012_d687"
result = result and format(-1234567, "#012_x") == "-0x0012_d687"

comma_hex_error = False
try:
    format(1234567, ",x")
except ValueError:
    comma_hex_error = True

underscore_char_error = False
try:
    format(65, "_c")
except ValueError:
    underscore_char_error = True

comma_char_error = False
try:
    format(65, ",c")
except ValueError:
    comma_char_error = True

result = result and comma_hex_error and underscore_char_error and comma_char_error

assert result
result
