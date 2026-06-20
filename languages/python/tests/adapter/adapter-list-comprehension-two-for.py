x = 100
values = [i * 10 + j for i in range(4) for j in range(i)]
result = values == [10, 20, 21, 30, 31, 32] and x == 100

letters = [a + b for a in "ab" for b in "xy"]
result = result and letters == ["ax", "ay", "bx", "by"]

empty = [i for i in range(3) for j in range(0)]
result = result and empty == []

assert result
result
