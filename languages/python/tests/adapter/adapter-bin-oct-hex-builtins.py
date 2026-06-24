assert bin(0) == "0b0"
assert bin(1) == "0b1"
assert bin(-1) == "-0b1"
assert bin(10) == "0b1010"
assert bin(True) == "0b1"
assert bin(False) == "0b0"
assert bin(2 ** 65) == "0b1" + "0" * 65
assert bin(2 ** 65 - 1) == "0b" + "1" * 65
assert bin(-(2 ** 65)) == "-0b1" + "0" * 65
assert bin(-(2 ** 65 - 1)) == "-0b" + "1" * 65

assert oct(0) == "0o0"
assert oct(8) == "0o10"
assert oct(100) == "0o144"
assert oct(-100) == "-0o144"
assert oct(True) == "0o1"

assert hex(0) == "0x0"
assert hex(16) == "0x10"
assert hex(255) == "0xff"
assert hex(-16) == "-0x10"
assert hex(-42) == "-0x2a"
assert hex(False) == "0x0"

bin_type_error = False
try:
    bin({})
except TypeError:
    bin_type_error = True

oct_type_error = False
try:
    oct(())
except TypeError:
    oct_type_error = True

hex_type_error = False
try:
    hex("1")
except TypeError:
    hex_type_error = True

float_type_error = False
try:
    bin(1.0)
except TypeError:
    float_type_error = True

result = bin_type_error and oct_type_error and hex_type_error and float_type_error
result
