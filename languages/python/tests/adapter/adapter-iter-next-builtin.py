result = True

pair = iter([1, 2])
result = result and bool(pair) == True
result = result and next(pair) == 1
result = result and next(pair) == 2

sink_count = 0
try:
    next(pair)
except StopIteration:
    sink_count += 1
try:
    next(pair)
except StopIteration:
    sink_count += 1
result = result and sink_count == 2
result = result and next(pair, 42) == 42

alias_a = iter([7, 8])
alias_b = alias_a
result = result and next(alias_b) == 7
result = result and next(alias_a) == 8
result = result and next(alias_b, 99) == 99

outer = iter([5, 6])
inner = iter(outer)
result = result and next(inner) == 5
result = result and next(outer) == 6

chars = iter("ab")
result = result and next(chars) == "a"
result = result and next(chars) == "b"
result = result and next(chars, "done") == "done"

byte_values = iter(b"\x00\x02")
result = result and next(byte_values) == 0
result = result and list(byte_values) == [2]
result = result and list(byte_values) == []

drain = iter((3, 4))
result = result and list(drain) == [3, 4]
result = result and list(drain) == []

tuple_drain = iter(range(0, 3))
result = result and tuple(tuple_drain) == (0, 1, 2)
result = result and next(tuple_drain, 99) == 99

temp_next = next(iter([9]))
result = result and temp_next == 9
result = result and next(iter([]), 10) == 10

loop_it = iter([10, 20, 30])
loop_total = 0
for value in loop_it:
    loop_total += value
    if value == 20:
        break
result = result and loop_total == 30
result = result and next(loop_it) == 30
result = result and next(loop_it, 40) == 40

continue_it = iter([1, 2, 3])
continue_total = 0
for value in continue_it:
    if value == 2:
        continue
    continue_total += value
else:
    continue_total += 10
result = result and continue_total == 14
result = result and next(continue_it, 99) == 99

marker = 0
for value in iter([]):
    marker = 1
else:
    marker = 2
result = result and marker == 2

bad_iter_arity = False
try:
    iter()
except TypeError:
    bad_iter_arity = True

bad_iter_value = False
try:
    iter(1)
except TypeError:
    bad_iter_value = True

bad_iter_sentinel_callable = False
try:
    iter(1, 2)
except TypeError:
    bad_iter_sentinel_callable = True

bad_next_arity = False
try:
    next()
except TypeError:
    bad_next_arity = True

bad_next_value = False
try:
    next([1])
except TypeError:
    bad_next_value = True

empty_stop = False
try:
    next(iter([]))
except StopIteration:
    empty_stop = True

result = (
    result
    and bad_iter_arity
    and bad_iter_value
    and bad_iter_sentinel_callable
    and bad_next_arity
    and bad_next_value
    and empty_stop
)
assert result
result
