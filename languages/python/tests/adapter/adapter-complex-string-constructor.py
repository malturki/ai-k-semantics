result = complex("1") == complex(1, 0)
result = result and complex("-1") == complex(-1, 0)
result = result and complex("+1") == complex(1, 0)
result = result and complex("1.5") == complex(1.5, 0)
result = result and complex(" -2.5e-1 ") == complex(-0.25, 0)
result = result and complex("1j") == complex(0, 1)
result = result and complex("-1J") == complex(0, -1)
result = result and complex("J") == complex(0, 1)
result = result and complex("+j") == complex(0, 1)
result = result and complex("-j") == complex(0, -1)
result = result and complex(" -2.5e-1j ") == complex(0, -0.25)
assert result
result
