parts = {"real": 4.25, "imag": 1.5}
imag_only = {"imag": 1.5}
real_only = {"real": 4.25}
bool_parts = {"imag": False, "real": True}

result = complex(**parts) == (4.25 + 1.5j)
result = result and complex(4.25, **imag_only) == (4.25 + 1.5j)
result = result and complex(real=4.25, **imag_only) == (4.25 + 1.5j)
result = result and complex(**real_only, **imag_only) == (4.25 + 1.5j)
result = result and complex(**bool_parts) == (1 + 0j)
assert result
result
