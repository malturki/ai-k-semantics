int_nbsp = int("\u00a012\u00a0") == 12
int_em_space = int("\u200312\u2029") == 12
int_ideographic_negative = int("\u3000-12\u205f") == -12
int_explicit_base = int("\u00a0ff\u00a0", 16) == 255
int_base_zero = int("\u20030b101\u2029", 0) == 5

float_nbsp = float("\u00a012.5\u00a0") == 12.5
float_em_space = float("\u2003-2.5e1\u2029") == -25.0
float_special = float("\u205finf\u3000") == float("inf")

int_c0_separator = False
try:
    int("\u001c12\u001f")
except ValueError:
    int_c0_separator = True

float_c0_separator = False
try:
    float("\u001c12\u001f")
except ValueError:
    float_c0_separator = True

int_utf8_space_bytes = False
try:
    int(b"\xe2\x80\x8312\xe2\x80\x83")
except ValueError:
    int_utf8_space_bytes = True

float_utf8_space_bytes = False
try:
    float(b"\xe2\x80\x8312.5\xe2\x80\x83")
except ValueError:
    float_utf8_space_bytes = True

int_utf8_space_bytearray = False
try:
    int(bytearray(b"\xe2\x80\x8312\xe2\x80\x83"))
except ValueError:
    int_utf8_space_bytearray = True

float_utf8_space_bytearray = False
try:
    float(bytearray(b"\xe2\x80\x8312.5\xe2\x80\x83"))
except ValueError:
    float_utf8_space_bytearray = True

result = (
    int_nbsp
    and int_em_space
    and int_ideographic_negative
    and int_explicit_base
    and int_base_zero
    and float_nbsp
    and float_em_space
    and float_special
    and int_c0_separator
    and float_c0_separator
    and int_utf8_space_bytes
    and float_utf8_space_bytes
    and int_utf8_space_bytearray
    and float_utf8_space_bytearray
)
assert result
result
