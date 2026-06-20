x = 7

values = {
    i * 100 + j * 10 + k: i + j + k
    for i in range(2)
    for j in range(i + 1)
    for k in range(j + 1)
}
result = values == {0: 0, 100: 1, 110: 2, 111: 3} and x == 7

duplicates = {
    j: i * 10 + j
    for i in range(3)
    for j in range(2)
    for k in range(1)
}
result = result and duplicates == {0: 20, 1: 21}

empty_middle = {
    i: i
    for i in range(2)
    for j in range(0)
    for k in range(1)
}
result = result and empty_middle == {}

empty_inner = {
    i: i
    for i in range(2)
    for j in range(1)
    for k in range(0)
}
result = result and empty_inner == {}

assert result
result
