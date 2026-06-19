capture = lambda head, *tail: head == 1 and tail == (2, 3)
empty = lambda *items: items == ()
result = capture(1, 2, 3)
result = result and empty()
assert result
result
