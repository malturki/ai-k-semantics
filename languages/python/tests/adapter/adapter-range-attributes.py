simple = range(4)
result = simple.start == 0 and simple.stop == 4 and simple.step == 1

bounded = range(2, 7)
result = result and bounded.start == 2 and bounded.stop == 7 and bounded.step == 1

descending = range(7, 2, -2)
result = result and descending.start == 7 and descending.stop == 2 and descending.step == -2

empty = range(3, 3)
result = result and empty.start == 3 and empty.stop == 3 and empty.step == 1

computed = range(1, 8, 3)
result = result and computed.start + computed.stop + computed.step == 12

assert result
result
