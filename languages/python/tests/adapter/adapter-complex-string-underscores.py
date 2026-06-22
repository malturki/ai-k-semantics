result = complex("4_2") == complex(42, 0)
result = result and complex("1_00_00.5") == complex(10000.5, 0)
result = result and complex(".1_4") == complex(0.14, 0)
result = result and complex("1_00_00j") == complex(0, 10000)
result = result and complex("1_00_00.5j") == complex(0, 10000.5)
result = result and complex(".1_4j") == complex(0, 0.14)
result = result and complex("1_2.5+3_3j") == complex(12.5, 33)
result = result and complex("(1_2.5+3_3j)") == complex(12.5, 33)
result = result and complex("(.5_6j)") == complex(0, 0.56)
assert result
result
