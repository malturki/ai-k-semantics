result = (x := 3) == 3
result = result and x == 3
result = result and ((y := x + 2) == 5)
result = result and y == 5
flag = True
result = result and ((False if (flag := False) else True) == True)
result = result and flag == False
right = 0
result = result and (((left := False) and (right := 1)) == False)
result = result and left == False
result = result and right == 0
count = 0
while (count := count + 1) < 4:
    pass
result = result and count == 4
assert result
result
