z = 3 + 4j

result = ((1 + 2j) * (3 + 4j)) == (-5 + 10j)
result = result and z * 2 == (6 + 8j)
result = result and 2 * z == (6 + 8j)
result = result and z * 0.5 == (1.5 + 2j)
result = result and 0.5 * z == (1.5 + 2j)

result = result and z / 2 == (1.5 + 2j)
result = result and z / 0.5 == (6 + 8j)
result = result and z / (1 + 1j) == (3.5 + 0.5j)
result = result and (1 + 1j) / (1 - 1j) == 1j
result = result and 2 / (1 + 1j) == (1 - 1j)
result = result and 4.0 / (1 - 1j) == (2 + 2j)

assert result
result
