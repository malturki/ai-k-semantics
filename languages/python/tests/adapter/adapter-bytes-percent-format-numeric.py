fmt = b"%d:%i:%u:%o:%x:%X"
value = fmt % (12, -7, True, 10, 255, 255)

signed = b"%d|%i|%u|%o|%x|%X" % (-42, -42, -42, -10, -255, -255)
float_decimal = b"%d:%i:%u:%d" % (1.9, -1.9, -0.4, False)
single = b"%x" % 3735928559

result = (
    value == b"12:-7:1:12:ff:FF"
    and signed == b"-42|-42|-42|-12|-ff|-FF"
    and float_decimal == b"1:-1:0:0"
    and single == b"deadbeef"
)

assert result
result
