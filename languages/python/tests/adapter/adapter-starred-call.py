def pack(a, b, c, d=4):
    return a * 1000 + b * 100 + c * 10 + d

def total3(a, b, c):
    return a + b + c

items = [2, 3]
result = pack(1, *items) == 1234
result = result and pack(*range(1, 4), d=4) == 1234
result = result and total3(1, *{2, 3}) == 6
assert result
result
