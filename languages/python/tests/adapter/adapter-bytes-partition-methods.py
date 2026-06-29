data = b"a:b:c"

partition_ok = (
    data.partition(b":") == (b"a", b":", b"b:c")
)

rpartition_ok = (
    data.rpartition(b":") == (b"a:b", b":", b"c")
)

result = partition_ok and rpartition_ok and data == b"a:b:c"
assert result
result
