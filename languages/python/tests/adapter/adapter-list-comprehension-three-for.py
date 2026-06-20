x = 5

values = [i * 100 + j * 10 + k for i in range(2) for j in range(i + 1) for k in range(j + 1)]
result = values == [0, 100, 110, 111] and x == 5

letters = [a + b + c for a in "ab" for b in "x" for c in "12"]
result = result and letters == ["ax1", "ax2", "bx1", "bx2"]

empty_middle = [i for i in range(2) for j in range(0) for k in range(1)]
result = result and empty_middle == []

empty_inner = [i for i in range(2) for j in range(2) for k in range(0)]
result = result and empty_inner == []

assert result
result
