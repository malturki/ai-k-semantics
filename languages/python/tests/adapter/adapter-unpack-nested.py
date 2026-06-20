(a, (b, c), [d, e]) = (1, (2, 3), [4, 5])
result = a == 1 and b == 2 and c == 3 and d == 4 and e == 5

[x, (y, z)] = [6, [7, 8]]
result = result and x == 6 and y == 7 and z == 8

((same,), same) = ((9,), 10)
result = result and same == 10

((sa, sb),) = {(11, 12)}
result = result and sa == 11 and sb == 12

left, (set_a, set_b) = (0, {13, 14})
result = result and left == 0 and {set_a, set_b} == {13, 14}

assert result
result
