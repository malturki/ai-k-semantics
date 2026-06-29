terminal = b"One line\n"

result = terminal.splitlines() == [b"One line"] and terminal.splitlines(True) == [b"One line\n"]
assert result
result
