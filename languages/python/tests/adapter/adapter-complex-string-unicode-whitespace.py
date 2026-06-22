result = complex("\u00a01+2j\u00a0") == complex(1, 2)
result = result and complex("\u2003infj\u2029") == complex(0, float("inf"))
result = result and complex("\u2028(inf-infj)\u2029") == complex(float("inf"), -float("inf"))
z = complex("\u205fnan\u3000")
result = result and z.real != z.real and z.imag == 0
assert result
result
