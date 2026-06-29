dash = bytearray(b"-")

bad_item_ok = True
try:
    dash.join([b"a", "b"])
    bad_item_ok = False
except TypeError:
    pass

bad_iter_ok = True
try:
    dash.join(123)
    bad_iter_ok = False
except TypeError:
    pass

result = bad_item_ok and bad_iter_ok and dash == bytearray(b"-")
assert result
result
