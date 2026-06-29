data = b"banana"
empty = b""

result = (
    data.find(b"ana") == 1
    and data.find(bytearray(b"na")) == 2
    and data.find(memoryview(b"na")) == 2
    and data.find(b"") == 0
    and data.find(bytearray()) == 0
    and data.find(memoryview(b"")) == 0
    and data.find(b"zz") == -1
    and empty.find(b"") == 0
    and data.rfind(b"ana") == 3
    and data.rfind(bytearray(b"na")) == 4
    and data.rfind(memoryview(b"na")) == 4
    and data.rfind(b"") == 6
    and data.rfind(bytearray()) == 6
    and data.rfind(memoryview(b"")) == 6
    and data.rfind(b"zz") == -1
    and empty.rfind(b"") == 0
    and data == b"banana"
)

assert result
result
