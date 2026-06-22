result = complex("1+2j") == complex(1, 2)
result = result and complex("1-1j") == complex(1, -1)
result = result and complex("-1+2j") == complex(-1, 2)
result = result and complex("+1-2J") == complex(1, -2)
result = result and complex("1.5+4.25j") == complex(1.5, 4.25)
result = result and complex("4.25+1J") == complex(4.25, 1)
result = result and complex("1e2+3e1j") == complex(100, 30)
result = result and complex("1e-2-3e-1j") == complex(0.01, -0.3)
result = result and complex("4.25+j") == complex(4.25, 1)
result = result and complex("4.25-J") == complex(4.25, -1)
assert result
result
