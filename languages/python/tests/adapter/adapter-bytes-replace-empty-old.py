abc = b"abc"
empty = b""

empty_old_ok = (
    abc.replace(b"", b"-") == b"-a-b-c-"
    and abc.replace(b"", b"-", 1) == b"-abc"
    and abc.replace(b"", b"-", 2) == b"-a-bc"
    and abc.replace(b"", b"-", 3) == b"-a-b-c"
    and abc.replace(b"", b"-", 4) == b"-a-b-c-"
    and abc.replace(b"", b"-", 0) == b"abc"
    and empty.replace(b"", b"-") == b"-"
    and empty.replace(b"", b"-", 0) == b""
)

empty_new_ok = (
    abc.replace(b"", b"") == b"abc"
    and empty.replace(b"", b"") == b""
)

unchanged_ok = abc == b"abc" and empty == b""

result = empty_old_ok and empty_new_ok and unchanged_ok
assert result
result
