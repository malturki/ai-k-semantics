result = complex("(1+2j)") == complex(1, 2)
result = result and complex("(1.5+4.25j)") == complex(1.5, 4.25)
result = result and complex(" ( +4.25-6J )") == complex(4.25, -6)
result = result and complex(" ( +4.25-J )") == complex(4.25, -1)
result = result and complex(" ( +4.25+j )") == complex(4.25, 1)
result = result and complex("( j )") == complex(0, 1)
result = result and complex("( -j)") == complex(0, -1)
assert result
result
