z = complex("nan")
result = z.real != z.real and z.imag == 0
z = complex("+NaNj")
result = result and z.real == 0 and z.imag != z.imag
z = complex("-nan+nanj")
result = result and z.real != z.real and z.imag != z.imag
z = complex("(nan-nanj)")
result = result and z.real != z.real and z.imag != z.imag
assert result
result
