caught_plain = False
try:
    assert False
except AssertionError:
    caught_plain = True

msg_seen = False
caught_msg = False
try:
    assert False, (msg_seen := True)
except AssertionError:
    caught_msg = msg_seen is True

skip_seen = True
assert True, (skip_seen := False)
skip_ok = skip_seen is True

wrong_handler = False
right_handler = False
try:
    assert 0
except ValueError:
    wrong_handler = True
except AssertionError:
    right_handler = True

result = caught_plain and caught_msg and skip_ok and right_handler and not wrong_handler
assert result
result
