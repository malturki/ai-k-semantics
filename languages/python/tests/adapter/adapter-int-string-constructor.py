result = int("0") == 0
result = result and int("123") == 123
result = result and int("-42") == -42
result = result and int("+7") == 7
result = result and int("101", 2) == 5
result = result and int("77", 8) == 63
result = result and int("ff", 16) == 255
result = result and int("FF", 16) == 255
result = result and int("z", 36) == 35
result = result and int("-z", 36) == -35

assert result
result
