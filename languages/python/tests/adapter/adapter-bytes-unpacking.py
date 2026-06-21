a, b = b"AZ"
result = a == 65 and b == 90

first, *middle, last = b"abcd"
result = result and first == 97 and middle == [98, 99] and last == 100

*empty, = b""
result = result and empty == []

top, (left, right) = (7, b"xy")
result = result and top == 7 and left == 120 and right == 121

pair_total = 0
for p, q in [b"ab", b"cd"]:
    pair_total += p + q

result = result and pair_total == 97 + 98 + 99 + 100

nested_total = 0
for outer, (inner_left, inner_right) in [(5, b"bc")]:
    nested_total = outer + inner_left + inner_right

result = result and nested_total == 5 + 98 + 99

star_total = 0
for head, *rest, tail in [b"abc", b"xy"]:
    star_total += head + sum(rest) + tail

result = result and star_total == 97 + 98 + 99 + 120 + 121

empty_item = False
for *empty_item, in [b""]:
    empty_item = empty_item == []

result = result and empty_item
result
