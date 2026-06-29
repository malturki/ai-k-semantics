data = b"banana"
bool_data = bytes([0, 1, 1])
empty = b""

result = (
    data.find(97) == 1
    and data.find(120) == -1
    and bool_data.find(True) == 1
    and data.rfind(97) == 5
    and data.rfind(120) == -1
    and bool_data.rfind(True) == 2
    and empty.find(1) == -1
    and empty.rfind(1) == -1
    and data == b"banana"
)

assert result
result
