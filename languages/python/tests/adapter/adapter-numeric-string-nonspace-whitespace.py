result = int("\t123\n") == 123
result = result and int("\v-42\f") == -42
result = result and int("\r+0x10\t", 0) == 16
result = result and float("\n1.5\t") == 1.5
result = result and float("\r-2.5e-1\f") == -0.25

assert result
result
