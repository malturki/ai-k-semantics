a, b = "xy"
result = a == "x" and b == "y"

first, *middle, last = "wxyz"
result = result and first == "w" and middle == ["x", "y"] and last == "z"

*empty_string, = ""
result = result and empty_string == []

r0, r1, r2 = range(1, 4)
result = result and r0 == 1 and r1 == 2 and r2 == 3

head, *tail = range(3, 0, -1)
result = result and head == 3 and tail == [2, 1]

*empty_range, = range(0)
result = result and empty_range == []

((c, d),) = ["hi"]
result = result and c == "h" and d == "i"

((m, n),) = [range(5, 7)]
result = result and m == 5 and n == 6

assert result
result
