empty = str()
assert empty == ""

result = str(7) + ":" + str(True) + ":" + str(False) + ":" + str(None) + ":" + str(...)
assert result == "7:True:False:None:Ellipsis"

name = "Ada"
result = str(name) + ":" + repr(name) + ":" + ascii(name)
assert result == "Ada:'Ada':'Ada'"

x = 0
result = str((x := 5)) + ":" + repr(x) + ":" + ascii(False)
assert result == "5:5:False"

result == "5:5:False"
