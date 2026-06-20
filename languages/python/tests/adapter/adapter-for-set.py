total = 0
count = 0
for value in {3, 1, 2}:
    total += value
    count += 1

empty_else = False
for value in set():
    empty_else = False
else:
    empty_else = True

normal_else = False
for value in {4}:
    total += value
else:
    normal_else = True

break_suppressed = False
for value in {9, 10}:
    break_suppressed = True
    break
else:
    break_suppressed = False

pair_total = 0
pair_count = 0
for a, b in {(1, 2), (3, 4)}:
    pair_total += a + b
    pair_count += 1

star_total = 0
star_count = 0
for head, *middle, tail in {(1, 2, 3), (4, 5, 6)}:
    star_total += head + tail + len(middle)
    star_count += 1

unpack_empty_else = False
for a, b in set():
    unpack_empty_else = False
else:
    unpack_empty_else = True

star_empty_else = False
for head, *middle in set():
    star_empty_else = False
else:
    star_empty_else = True

result = total == 10 and count == 3
result = result and empty_else and normal_else and break_suppressed
result = result and pair_total == 10 and pair_count == 2
result = result and star_total == 16 and star_count == 2
result = result and unpack_empty_else and star_empty_else

assert result
result
