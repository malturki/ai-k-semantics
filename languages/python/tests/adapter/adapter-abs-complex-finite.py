result = abs(3 + 4j) == 5.0
result = result and abs(5j) == 5.0
result = result and abs(0j) == 0.0
result = result and abs(1 + 0j) == 1.0
result = result and abs(-3 - 4j) == 5.0
assert result
result
