z = 3 + 4j

result = z.conjugate() == (3 - 4j)
result = result and (1j).conjugate() == -1j
result = result and complex(1.5, -2.5).conjugate() == (1.5 + 2.5j)
result = result and (3).conjugate() == 3
result = result and (-2).conjugate() == -2
result = result and True.conjugate() == 1
result = result and False.conjugate() == 0
result = result and (1.5).conjugate() == 1.5
assert result
result
