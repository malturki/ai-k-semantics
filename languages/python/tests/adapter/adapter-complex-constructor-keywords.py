result = complex(real=4.25) == (4.25 + 0j)
result = result and complex(imag=1.5) == 1.5j
result = result and complex(real=4.25, imag=1.5) == (4.25 + 1.5j)
result = result and complex(imag=1.5, real=4.25) == (4.25 + 1.5j)
result = result and complex(4.25, imag=1.5) == (4.25 + 1.5j)
result = result and complex(True, imag=False) == (1 + 0j)
result = result and complex(real=True, imag=False) == (1 + 0j)
assert result
result
