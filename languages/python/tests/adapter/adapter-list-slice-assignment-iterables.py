chars = [0]
chars[0:1] = "ab"

bytes_rhs = [0, 0]
bytes_rhs[:1] = b"AZ"

dict_rhs = [0]
dict_rhs[:] = {"x": 1, "y": 2}

set_rhs = [0]
set_rhs[:] = {3, 4}

range_rhs = [0]
range_rhs[:] = range(2, 5)

empty_rhs = [1, 2, 3]
empty_rhs[1:3] = ""

ext = [0, 1, 2, 3]
ext[::2] = "ab"

extb = [0, 1, 2, 3]
extb[1::2] = b"AZ"

extr = [0, 1, 2, 3, 4, 5]
extr[5:0:-2] = range(7, 10)

extempty = [1, 2]
extempty[5:5:2] = range(0)

result = (
    chars == ["a", "b"]
    and bytes_rhs == [65, 90, 0]
    and dict_rhs == ["x", "y"]
    and set(set_rhs) == {3, 4}
    and range_rhs == [2, 3, 4]
    and empty_rhs == [1]
    and ext == ["a", 1, "b", 3]
    and extb == [0, 65, 2, 90]
    and extr == [0, 9, 2, 8, 4, 7]
    and extempty == [1, 2]
)
assert result
result
