values = [0, 1, 2, 3, 4]
result = values[slice(1, 4)] == [1, 2, 3]
result = result and values[slice(None, None, -1)] == [4, 3, 2, 1, 0]

letters = "abcdef"
result = result and letters[slice(1, 5, 2)] == "bd"

items = (0, 1, 2, 3, 4)
result = result and items[slice(0, 5, 2)] == (0, 2, 4)

r = range(10)
result = result and r[slice(2, 8, 2)] == range(2, 8, 2)

s = slice(1, 4)
result = result and s.start == 1 and s.stop == 4 and s.step == None
result = result and slice(4).start == None and slice(4).stop == 4 and slice(4).step == None
result = result and slice(1, 4, 2) == slice(1, 4, 2)
result = result and bool(slice(None, None, None))

assert result
result
