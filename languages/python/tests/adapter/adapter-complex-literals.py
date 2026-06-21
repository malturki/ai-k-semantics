imag = 1j
zero = 0j
literal = 3 + 4j
mixed = 3.5 - 2j

result = imag == 1j
result = result and zero == 0j
result = result and not bool(zero)
result = result and bool(imag)
result = result and literal == (3 + 4j)
result = result and mixed == (3.5 - 2j)
result = result and (1 + 0j) == 1
result = result and 1 == (1 + 0j)
result = result and (1.5 + 0j) == 1.5
result = result and True == (1 + 0j)
result = result and False == 0j
result = result and +(1j) == 1j
result = result and -(1j) == -1j
result = result and (1j + 2j) == 3j
result = result and (3j - 1j) == 2j
result = result and (3 - 2j) == (3 + (-2j))

assert result
result
