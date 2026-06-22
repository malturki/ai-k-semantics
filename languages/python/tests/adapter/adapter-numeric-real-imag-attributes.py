z = 3 + 4j

result = z.real == 3.0 and z.imag == 4.0
result = result and (1j).real == 0.0 and (1j).imag == 1.0
result = result and complex(1.5, -2.5).real == 1.5
result = result and complex(1.5, -2.5).imag == -2.5
result = result and (3).real == 3 and (3).imag == 0
result = result and (-2).real == -2 and (-2).imag == 0
result = result and True.real == 1 and True.imag == 0
result = result and False.real == 0 and False.imag == 0
result = result and (3).numerator == 3 and (3).denominator == 1
result = result and (-2).numerator == -2 and (-2).denominator == 1
result = result and True.numerator == 1 and True.denominator == 1
result = result and False.numerator == 0 and False.denominator == 1
result = result and (1.5).real == 1.5 and (1.5).imag == 0.0
assert result
result
