result = complex() == 0j
result = result and complex(1) == (1 + 0j)
result = result and complex(True) == (1 + 0j)
result = result and complex(False) == 0j
result = result and complex(1.5) == (1.5 + 0j)
result = result and complex(1 + 2j) == (1 + 2j)
result = result and complex(1, 2) == (1 + 2j)
result = result and complex(1.5, 2.5) == (1.5 + 2.5j)
result = result and complex(True, False) == (1 + 0j)

assert result
result
