z = 1 + 2j

result = z ** 0 == (1 + 0j)
result = result and z ** 1 == (1 + 2j)
result = result and z ** 2 == (-3 + 4j)
result = result and z ** 3 == (-11 - 2j)
result = result and pow(z, 2) == (-3 + 4j)
result = result and pow(2 + 0j, -2) == (0.25 + 0j)
result = result and pow(1j, 2) == (-1 + 0j)
result = result and pow(1j, -1) == -1j
result = result and pow(0j, 0) == (1 + 0j)
result = result and pow(2 + 3j, True) == (2 + 3j)
result = result and pow(2 + 3j, False) == (1 + 0j)

assert result
result
