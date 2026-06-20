x = 71

values = {
    i * 100 + j * 10 + k
    for i in range(3)
    for j in range(i + 1)
    for k in range(j + 1)
}
result = values == {0, 100, 110, 111, 200, 210, 211, 220, 221, 222} and x == 71

dupes = {j for i in range(3) for j in range(2) for k in range(2)}
result = result and dupes == {0, 1}

empty = {i * 10 + j + k for i in range(3) for j in range(i) for k in range(0)}
result = result and empty == set()

assert result
result
